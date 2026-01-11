#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from collections import OrderedDict

def load_locale_file(file_path):
    """Загружает и парсит JSON файл с переводами, сохраняя порядок ключей."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f, object_pairs_hook=OrderedDict)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга {file_path}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка чтения {file_path}: {e}")
        sys.exit(1)

def create_merged_structure(source, target):
    """Создает новую структуру, сохраняя порядок ключей из source и значения из target."""
    if not isinstance(source, dict) or not isinstance(target, dict):
        return target if target is not None else source

    result = OrderedDict()
    
    # Сначала добавляем все ключи из source в правильном порядке
    for key in source.keys():
        if key in target:
            # Если ключ есть в обоих словарях, рекурсивно обрабатываем вложенные словари
            result[key] = create_merged_structure(source[key], target[key])
        else:
            # Если ключа нет в целевом словаре, добавляем его с пометкой TODO
            print(f"Добавлен отсутствующий ключ: {key}")
            if isinstance(source[key], dict):
                # Для вложенных словарей создаем такую же структуру
                result[key] = create_merged_structure(source[key], OrderedDict())
            else:
                # Для простых значений добавляем с пометкой TODO
                result[key] = f"TODO: {source[key]}"
    
    return result

def save_locale_file(data, file_path):
    """Сохраняет JSON файл с отступами и сохранением порядка ключей."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=False)
        f.write('\n')  # Добавляем перевод строки в конец файла

def main():
    if len(sys.argv) != 3:
        print("Использование: python compare_locales_json.py <исходный_файл.json> <целевой_файл.json>")
        print("Пример: python compare_locales_json.py json/locale_en-US.json json/locale_ru-RU.json")
        return
    
    source_file = sys.argv[1]
    target_file = sys.argv[2]
    
    print(f"Загружаю исходный файл: {source_file}")
    source_locale = load_locale_file(source_file)
    
    print(f"Загружаю целевой файл: {target_file}")
    try:
        target_locale = load_locale_file(target_file)
    except FileNotFoundError:
        print(f"Файл {target_file} не найден. Будет создан новый.")
        target_locale = OrderedDict()
    
    print("\nОбновление структуры целевого файла...")
    merged_locale = create_merged_structure(source_locale, target_locale)
    
    # Создаем резервную копию перед сохранением
    backup_file = f"{target_file}.bak"
    print(f"\nСоздаю резервную копию: {backup_file}")
    try:
        import shutil
        shutil.copy2(target_file, backup_file)
    except Exception as e:
        print(f"Не удалось создать резервную копию: {e}")
    
    # Сохраняем обновленный файл
    print(f"Сохранение обновленного файла: {target_file}")
    save_locale_file(merged_locale, target_file)
    
    print("\nГотово! Целевой файл обновлен с сохранением порядка ключей из исходного файла.")
    print("Пожалуйста, найдите и переведите все строки, начинающиеся с 'TODO:'.")

if __name__ == "__main__":
    main()

# python3 compare_locales_json.py json/locale_en-US.json json/locale_ru-RU.json
