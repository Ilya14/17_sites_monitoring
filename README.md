# 17_sites_monitoring

## Описание

Скрипт для проверки состояния сайтов. Статус каждого сайта определяется
по результатам следующих проверок:

* сервер отвечает на запрос статусом HTTP 200;
* доменное имя сайта проплачено как минимум на 1 месяц вперед.

## Использование
Скрипт имеет следующие обязательные параметры:

* url_file - текстовый файл с URL адресами для проверки.

Скрипт имеет следующие опциональные параметры:

* -h, --help - помощь


## Пример

Отображение справки:

```sh
$ python3.5 ./check_sites_health.py -h
usage: check_sites_health.py [-h] url_file

Script for sites monitoring

positional arguments:
  url_file    Text file with URL addresses for check

optional arguments:
  -h, --help  show this help message and exit

```

Пример использования:

```sh
$ python3.5 ./check_sites_health.py ./sites.txt
1 URL: http://www.bmstu.ru/; STATUS 200: OK; EXPIRATION DATE: 2017-10-01 (VALID: OK)
2 URL: https://ru.wikipedia.org; STATUS 200: OK; EXPIRATION DATE: 2023-01-13 (VALID: OK)
3 URL: https://vk.com; STATUS 200: OK; EXPIRATION DATE: 2017-06-23 (VALID: OK)
4 URL: http://www.translate.ru/; STATUS 200: OK; EXPIRATION DATE: 2017-04-01 (VALID: OK)
```