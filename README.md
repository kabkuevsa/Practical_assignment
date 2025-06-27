# Form Template Finder

Программа для поиска шаблонов форм по переданным полям.

## 📦 Установка
1. Установите зависимости:
```bash
pip install -r requirements.txt
```

## 🚀 Использование
```bash
python app.py get_tpl --поле1=значение1 --поле2=значение2
```

### Примеры:
```bash
# Поиск шаблона
python app.py get_tpl --customer="Иван" --дата_заказа=01.01.2025

# Определение типов полей
python app.py get_tpl --неизвестное_поле=test@example.com
```

## 🧩 Структура проекта
- `app.py` — основной скрипт
- `db.py` — работа с базой данных (TinyDB)
- `validators.py` — проверка типов полей
- `tests/` — unit-тесты
- `templates.json` — база шаблонов форм