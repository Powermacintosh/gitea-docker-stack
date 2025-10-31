#!/bin/bash
set -euo pipefail

# ========================
# Конфигурация
# ========================

# Загружаем только нужные переменные
SERVICE_NAME=$(grep '^GITEA_SERVICE_NAME=' .env | cut -d '=' -f2-)
REGISTRY=$(grep '^GITEA_URL_REGISTRY=' .env | cut -d '=' -f2-)
REPO=$(grep '^GITEA_REPO=' .env | cut -d '=' -f2-)
USERNAME=$(grep '^DOCKER_HUB_USERNAME=' .env | cut -d '=' -f2-)
PASSWORD=$(grep '^DOCKER_HUB_TOKEN=' .env | cut -d '=' -f2-)
TELEGRAM_TOKEN=$(grep '^TELEGRAM_TOKEN=' .env | cut -d '=' -f2-)
TELEGRAM_CHAT_ID=$(grep '^TELEGRAM_CHAT_ID=' .env | cut -d '=' -f2-)

# ========================
# Авторизация в реестре
# ========================
if ! echo "$PASSWORD" | docker login "$REGISTRY" -u "$USERNAME" --password-stdin >/dev/null 2>&1; then
    echo "❌ Ошибка логина в Docker registry: $REGISTRY"
    exit 1
fi

# ========================
# Определяем версии
# ========================
CURRENT_TAG=$(docker service inspect "$SERVICE_NAME" --format '{{.Spec.TaskTemplate.ContainerSpec.Image}}' | awk -F: '{print $2}')
TAGS=$(curl -s -u "$USERNAME:$PASSWORD" "https://$REGISTRY/v2/$REPO/tags/list" | jq -r '.tags[]' | sort -V)
LATEST_TAG=$(echo "$TAGS" | tail -n1)

echo "Current tag: $CURRENT_TAG"
echo "Latest tag: $LATEST_TAG"

# ========================
# Сравниваем и обновляем
# ========================
if [ "$CURRENT_TAG" != "$LATEST_TAG" ]; then
    echo "🚀 Updating $SERVICE_NAME to version $LATEST_TAG..."
    docker pull "$REGISTRY/$REPO:$LATEST_TAG" >/dev/null
    docker service update --image "$REGISTRY/$REPO:$LATEST_TAG" "$SERVICE_NAME"

    # Уведомление в Telegram
    if [[ -n "${TELEGRAM_TOKEN:-}" && -n "${TELEGRAM_CHAT_ID:-}" ]]; then
        curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" \
            -d "chat_id=${TELEGRAM_CHAT_ID}" \
            -d "text=✅ Gitea обновлён до версии ${LATEST_TAG}" >/dev/null
    fi
else
    echo "✅ Service $SERVICE_NAME уже обновлён (версия $CURRENT_TAG)"
fi

