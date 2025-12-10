# Демонстрация обработки CSV

Это CLI-утилита на Python для обработки CSV-файлов с данными о производительности сотрудников и создания сводных отчётов.

![Демонстрация обработки CSV в терминале](demo.gif)

## Быстрый старт

### Требования

- [Python](https://www.python.org/downloads/) 3.13 - 3.14+ (протестировано, но может работать и на предыдущих версиях)
- Рекомендуется пакетный менеджер [uv](https://github.com/astral-sh/uv)

### Установка и запуск

Вы можете передать один или несколько файлов с помощью флага `--files` (для каждого файла свой флаг `--files`). По умолчанию используется отчёт `performance`, флаг и значение - `--report performance`, но этот флаг не обязательный.

В примерах я его не использую.

1. Склонируйте репозиторий

```bash
git clone https://github.com/iturdikulov/csv_processing_demo.git
cd csv_processing_demo
```

2.1 Запустите при помощи `uv` (автоматически создаться `env` окружение, подтянуться зависимости.

Набор файлов из интеграционных тестов:

```bash
uv run ./src/csv_processing/main.py \
--files ./tests/integration/data/empl_integration_01.csv ./tests/integration/data/empl_integration_02.csv
```

Набор файлов из ТЗ:

```bash
uv run ./src/csv_processing/main.py \
--files ./tests/unit/data/employees1.csv ./tests/unit/data/employees2.csv
```

Если всё работает переходите к пункту 3.

2.2 Альтернативный вариант. Установка и запуск как скрипта (`[project.scripts]` в `pyproject.toml`)

```bash
uv venv && uv sync
csv-processing \
--files ./tests/integration/data/empl_integration_01.csv ./tests/integration/data/empl_integration_02.csv
```

2.3 Альтернативный вариант, без `uv`.

```bash
python -m venv .venv

# активация под Linux/bash, у вас может быть другой шелл и другая команда
source .venv/bin/activate  

pip install -e .
python src/csv_processing/main.py \
--files ./tests/integration/data/empl_integration_01.csv ./tests/integration/data/empl_integration_02.csv
```

## Формат CSV

Входные CSV-файлы должны содержать как минимум следующие столбцы:

- `position`: Должность сотрудника.
- `performance`: Показатель производительности (числовое значение).

Файл обязательно должен содержать заголовок (header). Смотрите примеры в директории `./tests/integration/data/`.

## Тестирование

Для запуска тестов выполните:

```bash
uv run pytest
```

или

```bash
source .venv/bin/activate  # зависимости и virtualenv мы уже должны были настроить
pytest
```

## Нюансы и потенциальные улучшения

- Средний `performance` в отчёте я считаю для каждой группы профессий, в ТЗ про это не сказано, в реальном проекте я бы уточнил.
- Типизацию можно улучшить, но я обеспечил базовую поддержку.
- Комментарии и сообщения об ошибках на английском (я редко комментирую код на русском).
- Boilerplate проекта создан по шаблону пакета `uv init --package`, его довольно легко опубликовать в репозитории.
