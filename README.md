# quiz_app

Техническое задание "викторина".

Использовался следующий стэк

```
- flask
- flask_migrate
- flask-restful
- flask-script
- flask-sqlalchemy
- gunicorn
- markupsafe==2.0.0
- python-dotenv
- pip-compile-multi
- psycopg2
- psycopg2-binary
- requests
- wtforms
- werkzeug
```

## Установка и запуск(локально):

1. Скачать проект

   - git clone https://github.com/scad89/quiz_app.git

2. Добавить файл с переменными окружения(.env) в корень проекта

3. Активировать виртуальное окружение:

   - . venv_name/Scripts/activate - Windows
   - source venv_name/bin/activate - Linux

4. Установить зависимости(в виртуальном окружении):

   - pip install -r requirements.txt
     (после установки, зависимости можно обновить командой $ pip-compile -U)

5. Запустить сервер:

   - python app.py

Пример отправки POST запроса через Postman на адрес http://127.0.0.1:5000/question:
![](https://github.com/scad89/quiz_app/blob/main/image/postman_2.jpg)

## Установка и запуск(docker-compose):

```
WIP
```

## Contacts

- Instagram: [@igor*komkov*](https://www.instagram.com/igor_komkov_/)
- Vk.com: [Igor Komkov](https://vk.com/zzzscadzzz)
- Linkedin: [Igor Komkov](https://www.linkedin.com/in/igor-komkov/)
- email: **scad200@gmail.com**
- Telegram: **@zzzSCADzzz**
