# Toolshop QA Automation

Демо-проект автоматизации тестирования интернет-магазина
[Practice Software Testing (Toolshop)](https://practicesoftwaretesting.com).

## Стек

- Python, pytest
- requests, jsonschema — API-тесты
- Playwright — UI-тесты (Page Object Model)
- Allure — отчёты
- GitHub Actions — CI

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/SuzannaZhambeeva/toolshop-qa-automation.git
cd toolshop-qa-automation
```

### 2. Создать и включить виртуальное окружение

Создать (один раз):

```bash
python3 -m venv venv
```

Включить (каждый раз при открытии нового терминала):

```bash
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

Выключить:

```bash
deactivate
```

### 3. Установить зависимости

Тесты не запустятся без библиотек из `requirements.txt`.
Устанавливать нужно при включённом виртуальном окружении:

```bash
pip install -r requirements.txt
```

Для UI-тестов дополнительно нужен браузер

```bash
playwright install chromium
```

### 4. Запустить тесты

```bash
pytest                  # все тесты
pytest tests/api        # только API-тесты
pytest tests/ui         # только UI-тесты
pytest -m smoke         # только smoke-тесты
```

## Статус

- [x] Зависимости
- [ ] API-тесты
- [ ] UI-тесты
- [ ] CI и отчёты