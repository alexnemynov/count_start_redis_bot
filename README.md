# Телеграм бот, который считает нажатия команды /start и хранит их числ омежду запусками с помощью Redis

Команды:

/start - запустить бота.


# Зависимости 

    Python 3.12

# Установка

1. Клонировать репозиторий.

2. Создание виртуального окружения и установка зависимостей:
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

4. Установить Redis

5. Создать файл `.env` и заполнить его по образцу из `.env.example`

6. Запустить Redis
```bash
redis-server
```

7. Запуcтить бот.

```bash
python3 main.py
```



