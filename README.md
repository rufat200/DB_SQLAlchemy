# DB_SQLAlchemy


Проект для работы с асинхронной базой данных SQLite с использованием SQLAlchemy. Включает создание таблиц и добавление данных с использованием асинхронных сессий.

## Основная структура проекта
```bash
DB_SQLAlchemy/                    
├── database/                   
│    ├── __init__.py            
│    ├── db.py             
│    ├── models.py          
│    └── utils.py      
└── main.py
```
## Основные функции:
- **Добавление новой книги:** Пользователь может добавить в свою базу данных название книги, определяя её жанр и автора.

- **Добавление нового автора:** Перед добавлением названия книги, пользователю необходимо создать автора.

- **Добавление нового жанра:** Также, перед добавлением названия новой книги, нужно создать жанр.

### Используемые технологии:
- Python3.11
- Библиотека [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) для упрощения работы с базами данных

## Установка
### 1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/rufat200/DB_SQLAlchemy.git
   cd DB_SQLAlchemy
   ```
### 2. Создайтке виртуальное окружение (Рекомендуется):
   Для Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   Для macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
### 3. Установка библиотек:
   Для Windows:
   ```bash
   pip install -r requirements.txt
   ```
   Для macOS/Linux:
   ```bash
   pip3 install -r requirements.txt
   ```

## Запуск кода
   Для Windows:
   ```bash
   python main.py
   ```
   Для macOS/Linux:
   ```bash
   python3 main.py
   ```