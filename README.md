
# Сайт "Мастерская цветов"
Подберем для вас букет за два шага, который идеально подойдет под вашу ситуацию.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корневом каталоге вашего приложения (рядом с `manage.py`) и запишите туда данные в формате `ПЕРЕМЕННАЯ=значение`.

- `DEBUG`  — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. По умолчанию `False`.
- `SECRET_KEY`  — секретный ключ проекта.
- `ALLOWED_HOSTS`  — смотри  [документацию Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts).

Пример содержимого `.env` файла:
```
SECRET_KEY='django-insecure-pw_dRxiyw^4Wn7n#!_**$-m^@4dRxiyw^4Wn7n#!ntb'
ALLOWED_HOSTS=localhost,127.0.0.1
DEBUG=False
```

Более подробная инструкция по настройке переменных окружения можно найти в соответствующем разделе на [django docs](https://docs.djangoproject.com/en/3.2/ref/settings/).

## Запуск

 Клонируйте репозиторий с Github:
```shell
https://github.com/rudenko-ks/flower_shop.git
```
- Создайте виртуальное окружение:
```shell
python -m venv .venv
source .venv/bin/activate
```

- Установите зависимости командой:
```shell
pip install -r requirements.txt
```

- Создайте файл  `.env`  и внесите в него переменные окружения.

- Создайте файл базы данных и сразу примените все миграции командой:
```shell
python manage.py migrate
```

- Создайте администратора сайта в базе данных:
```shell
python manage.py createsuperuser
```
- Запустите сервер командой:
```shell
python manage.py runserver
```

## Использование

Главная страница располагается по адресу http://localhost:8000/

---
В проекте принимали участие

* [Kirill Rudenko](https://github.com/rudenko-ks)
* [Sergey Pavlov](https://github.com/spawlov)
* ...
