# Telegram-bot для отправки изображений
Бот выполняет отправку изображений в телеграм канал в виде постов.

## Функциональные возможности
- Загружает снимки с сервисов SpaceX API, APOD NASA, EPIC NASA
- Именует снимки и выгружает в отдельную директорию
- После загрузки отправляет, через бота, на ваш телеграм канал, с заданным интервалом

## Требования
- Python 3.x
- Необходимые библиотеки Python (можно установить через pip):
  - `telegram-python-bot` _(версия не старше 13)_
  - `environs`
  - `requests`

## Инструкции по установке
1. Склонируйте репозиторий или загрузите файлы проекта.


2. Установите необходимые зависимости:
```
pip install -r requirements.txt
```


3. Укажите переменные окружения, а именно: 
- `DIRECTORY_FOR_DOWNLOAD_IMAGE`
- `TIME_INTERVAL_FOR_SEND`
- `API_KEY_NASA`
- `ID_LAUNCH_SPACEX`*,если не указать ID запуска, будет использован последний*
- `TELEGRAM_TOKEN`
- `ID_TELEGRAM_BOT`
- `CHAT_ID`
- `IMAGE_COUNT_APOD`,`IMAGE_COUNT_EPIC`_- необходимое количество снимков_

## Запустите бота
- Через командную строку командой `cd` перейдите в папку с ботом
- Запустите командой 
```
python main.py
```
