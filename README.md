# Gitea Docker Stack

- Пакет для быстрого запуска Gitea в Docker.
- Содержит:
  - Docker Compose файл для запуска Gitea
  - Конфигурационный файл для раннера Gitea
  - Конфигурационные файлы для сборки и отправки логов в Grafana
  - Документацию для разработчиков
  - Пример файла .env
  - Утилиту для обработки переводов
  - Папку с файлами для кастомизации Gitea
  - Готовая тема для Gitea

## Требования

- Docker
- Docker Compose

## Начало работы

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/powermacintosh/gitea-docker-stack.git
cd gitea-docker-stack
```

### 2. Переменные окружения

```bash
# Скопируйте файл .env.example в .env
cp .env.example .env

# Отредактируйте файл .env
vim .env
```

- Первый запуск делается с пустой переменной `GITEA_RUNNER_TOKEN`.
- Переменные окружения `GITEA_RUNNER_TOKEN` заполняете после регистрации раннера.

### 3. Запуск через docker-compose

```sh
docker-compose up --build -d   # сборка и запуск в фоновом режиме
docker-compose down            # остановка контейнеров
docker-compose up -d           # запуск в фоновом режиме

docker network ls              # посмотреть сети
```

<img src="gray_cat.svg" alt="Gray Cat" style="width:100%; height:auto;">
