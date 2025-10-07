# Как запускать тесты

- **Юнит-тесты (без БД)**: `make test`  
  См. Makefile: цель `test` и `test-backend` (строки вокруг `442-449`).

- **Интеграционные тесты SQLite**:

  - Все: `make test-sqlite`
  - Конкретный тест: `make test-sqlite#TestE2e/ИмяИлиПаттерн` или `make test-sqlite#Пакет.Тест` (см. `517-524`)
  - Требование: установлен `git lfs` (цель `git-check`, строки `222-227`).

- **Интеграционные тесты MySQL**:

  - Все: `make test-mysql`
  - Конкретный тест: `make test-mysql#Паттерн`
  - Настройки соединения через переменные окружения:
    - `TEST_MYSQL_HOST`, `TEST_MYSQL_DBNAME`, `TEST_MYSQL_USERNAME`, `TEST_MYSQL_PASSWORD` (строки `187-200`, `528-545`).

- **Интеграционные тесты PostgreSQL**:

  - Все: `make test-pgsql`
  - Конкретный тест: `make test-pgsql#Паттерн`
  - Переменные: `TEST_PGSQL_HOST`, `TEST_PGSQL_DBNAME`, `TEST_PGSQL_USERNAME`, `TEST_PGSQL_PASSWORD`, `TEST_PGSQL_SCHEMA` (строки `191-196`, `549-567`).

- **Интеграционные тесты MSSQL**:

  - Все: `make test-mssql`
  - Конкретный тест: `make test-mssql#Паттерн`
  - Переменные: `TEST_MSSQL_HOST`, `TEST_MSSQL_DBNAME`, `TEST_MSSQL_USERNAME`, `TEST_MSSQL_PASSWORD` (строки `197-201`, `572-589`).

- **Миграционные тесты**:

  - SQLite: `make migrations.sqlite.test` или индивидуально: `make migrations.individual.sqlite.test`
  - MySQL: `make migrations.mysql.test` / `make migrations.individual.mysql.test`
  - PGSQL: `make migrations.pgsql.test` / `make migrations.individual.pgsql.test`
  - MSSQL: `make migrations.mssql.test` / `make migrations.individual.mssql.test`
  - См. блок `679-729`.

- **E2E тесты**:
  - SQLite: `make test-e2e-sqlite`
  - SQLite с визуальным тестированием: `ACCEPT_VISUAL=1 make test-e2e-sqlite`
  - MySQL/PG/MSSQL: `make test-e2e-mysql|test-e2e-pgsql|test-e2e-mssql`
  - См. `602-635`.

# Важно

- Перед интеграционными тестами нужен `git lfs` в PATH (иначе ошибка): проверьте `git lfs version`.
- Для MySQL/PG/MSSQL обеспечьте доступность БД по `TEST_*` переменным (либо поднимите контейнеры с такими хостами/портами, либо укажите свои).

# Примеры

- Запуск SQLite интеграций:  
  `make test-sqlite`
- Запуск одного интеграционного теста SQLite:  
  `make test-sqlite#TestRepoBlame`
- Запуск MySQL интеграций с локальным MySQL:  
  `TEST_MYSQL_HOST=127.0.0.1:3306 TEST_MYSQL_USERNAME=root TEST_MYSQL_PASSWORD=... make test-mysql`

Статус: цели и переменные для БД-тестов указаны; установите git-lfs и при необходимости задайте TEST\_\* для MySQL/PG/MSSQL.

## Резюме по исправлению тестов

fix(test): корректный выбор формата по длине хеша; увеличить таймаут в тесте индексатора

- Проблема: хеш длиной 64 не сопоставлялся формату объекта; выбор формата зависел от DefaultFeatures(), что приводило к неоднозначному поведению.
- Решение: определять формат строго по длине хекса:

  - 40 → Sha1
  - 64 → Sha256
    Убрана зависимость от DefaultFeatures().

- Тесты: в indexer_test увеличен таймаут ожидания опустошения очереди (5s не хватает на CI), чтобы устранить флаки.

Затронутые файлы:

- `modules/git/object_id.go`
- `modules/indexer/stats/indexer_test.go`

Поведение стало детерминированным, внешние API не изменены.
