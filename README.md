# Установка зависимостей

``python3 -m venv venv``

``source venv/bin/activate``

``pip3 install -r req.txt``

# Применение миграций

`` python manage.py migrate``

# Запуск

``python manage.py runserver localhost:8000`` - рус

``python manage.py runserver --settings=test_django.settings_kz localhost:9000`` - кз

**В БД уже есть пользователь (логин и пароль: root)**
и по 2 тестовые записи в каждой БД, их можно увидеть здесь: [рус](http://localhost:8000/test/)
и [кз](http://localhost:9000/test/)

! создание суперпользователя:
``python manage.py createsuperuser``
