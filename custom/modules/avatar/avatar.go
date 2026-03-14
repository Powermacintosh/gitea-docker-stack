// Copyright 2014 The Gogs Authors. All rights reserved.
// SPDX-License-Identifier: MIT

package avatar

import (
	"bytes"
	"errors"
	"fmt"
	"image"
	"image/color"
	"image/png"

	_ "image/gif"  // for processing gif images
	_ "image/jpeg" // for processing jpeg images

	"code.gitea.io/gitea/modules/avatar/identicon"
	"code.gitea.io/gitea/modules/setting"

	"golang.org/x/image/draw"

	_ "golang.org/x/image/webp" // for processing webp images
)

// DefaultAvatarSize is the target CSS pixel size for avatar generation. It is
// multiplied by setting.Avatar.RenderedSizeFactor and the resulting size is the
// usual size of avatar image saved on server, unless the original file is smaller
// than the size after resizing.
const DefaultAvatarSize = 256

// RandomImageWithSize generates and returns a random avatar image unique to input data
// in custom size (height and width).
func RandomImageWithSize(size int, data []byte) image.Image {
	// ИЗМЕНЕНО: используем color.Transparent вместо color.White для прозрачного фона
	imgMaker := identicon.New(size, color.Transparent, identicon.DarkColors)
	return imgMaker.Make(data)
}

// RandomImageDefaultSize generates and returns a random avatar image unique to input data
// in default size (height and width).
func RandomImageDefaultSize(data []byte) image.Image {
	return RandomImageWithSize(DefaultAvatarSize*setting.Avatar.RenderedSizeFactor, data)
}

// processAvatarImage process the avatar image data, crop and resize it if necessary.
// the returned data could be the original image if no processing is needed.
func processAvatarImage(data []byte, maxOriginSize int64) ([]byte, error) {
	imgCfg, imgType, err := image.DecodeConfig(bytes.NewReader(data))
	if err != nil {
		return nil, fmt.Errorf("image.DecodeConfig: %w", err)
	}

	// for safety, only accept known types explicitly
	if imgType != "png" && imgType != "jpeg" && imgType != "gif" && imgType != "webp" {
		return nil, errors.New("unsupported avatar image type")
	}

	// do not process image which is too large, it would consume too much memory
	if imgCfg.Width > setting.Avatar.MaxWidth {
		return nil, fmt.Errorf("image width is too large: %d > %d", imgCfg.Width, setting.Avatar.MaxWidth)
	}
	if imgCfg.Height > setting.Avatar.MaxHeight {
		return nil, fmt.Errorf("image height is too large: %d > %d", imgCfg.Height, setting.Avatar.MaxHeight)
	}

	// If the origin is small enough, just use it, then APNG could be supported,
	// otherwise, if the image is processed later, APNG loses animation.
	if len(data) < int(maxOriginSize) {
		return data, nil
	}

	img, _, err := image.Decode(bytes.NewReader(data))
	if err != nil {
		return nil, fmt.Errorf("image.Decode: %w", err)
	}

	// try to crop and resize the origin image if necessary
	img = cropSquare(img)

	targetSize := DefaultAvatarSize * setting.Avatar.RenderedSizeFactor
	img = scale(img, targetSize, targetSize, draw.BiLinear)

	// try to encode the cropped/resized image to png
	bs := bytes.Buffer{}
	if err = png.Encode(&bs, img); err != nil {
		return nil, err
	}
	resized := bs.Bytes()

	// usually the png compression is not good enough, use the original image if the origin is smaller
	if len(data) <= len(resized) {
		return data, nil
	}

	return resized, nil
}

// ProcessAvatarImage process the avatar image data, crop and resize it if necessary.
func ProcessAvatarImage(data []byte) ([]byte, error) {
	return processAvatarImage(data, setting.Avatar.MaxOriginSize)
}

// scale resizes the image to width x height using the given scaler.
func scale(src image.Image, width, height int, scale draw.Scaler) image.Image {
	rect := image.Rect(0, 0, width, height)
	// Используем NewRGBA для корректной поддержки прозрачности
	dst := image.NewRGBA(rect)
	// Предварительно заполняем прозрачным цветом
	draw.Draw(dst, rect, image.Transparent, image.Point{}, draw.Src)
	scale.Scale(dst, rect, src, src.Bounds(), draw.Over, nil)
	return dst
}

// cropSquare crops the largest square image from the center of the image.
func cropSquare(src image.Image) image.Image {
	bounds := src.Bounds()
	if bounds.Dx() == bounds.Dy() {
		return src
	}

	var rect image.Rectangle
	if bounds.Dx() > bounds.Dy() {
		size := bounds.Dy()
		rect = image.Rect((bounds.Dx()-size)/2, 0, (bounds.Dx()+size)/2, size)
	} else {
		size := bounds.Dx()
		rect = image.Rect(0, (bounds.Dy()-size)/2, size, (bounds.Dy()+size)/2)
	}

	dst := image.NewRGBA(rect)
	// Используем draw.Src для сохранения прозрачности при обрезке
	draw.Draw(dst, rect, src, rect.Min, draw.Src)
	return dst
}
