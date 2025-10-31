# Gitea Docker Stack: Production-Grade Deployment with Zero Downtime

## Структура проекта

- custom/ - кастомизация исходников
- deploy/ - для продакшн-развертывания
- docs/ - документация
- local/ - для локальной разработки
- locale-utils/ - для работы с локализацией исходников
- theme/ - готовые темы для релиза

## Требования

- Docker
- Docker Compose
- Docker Swarm

## Начало работы

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/powermacintosh/gitea-docker-stack.git
cd gitea-docker-stack
```

### 2. Переменные окружения

```bash
# Заполните файл .env
vim .env
```

- Первый запуск делается с пустой переменной `GITEA_RUNNER_TOKEN`.
- Переменные окружения `GITEA_RUNNER_TOKEN` заполняете после регистрации раннера.

### 3. Запуск docker-stack (для продакшн-развертывания)

#### 3.1. Инициализация Swarm

```sh
docker swarm init
```

#### 3.2. Запуск

```sh
docker stack deploy -c docker-stack.yml gitea
```

#### 3.3. Скрипт для обновления без задержки

```sh
./update-gitea.sh
```

### 4. Запуск через docker-compose

```sh
docker-compose up --build -d   # сборка и запуск в фоновом режиме
docker-compose down            # остановка контейнеров
docker-compose up -d           # запуск в фоновом режиме

docker network ls              # посмотреть сети
```

<img src="gray_cat.svg" alt="Gray Cat" style="width:100%; height:auto;">
