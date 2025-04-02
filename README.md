# Проект effective_mobile
Система управления заказами в кафе

## Для запуска приложения необходимо:
- создать файл .env с django SECRET_KEY как в файле .env.example
- для генерации django SECRET_KEY необходимо выполнить следующие команды в терминале:
```
from django.core.management import utils
utils.get_random_secret_key()
```
- запустить docker командой:
```
docker-compose up -d --build
```
## Для выполнения CRUD операции через веб-интерфейс необходимо зарегистрироваться и залогиниться,
## в противном случае пользователи могут только просматривать список существующих заказов на главной странице

## Существующие API-эндпоинты

OpenAPI (Swagger)
```
http://127.0.0.1/swagger/
```
## Postman Collection
[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://crimson-shadow-598593.postman.co/collection/15098807-c15ec737-215b-49e3-b5c1-02fb349f974a?source=rip_markdown&active-environment=15098807-0af2719b-4140-4ce8-87ef-86731d10708e)
> Не забудьте выбрать `EFFECTIVE MOBILE` environment
