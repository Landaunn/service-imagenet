# service-imagenet
В данном репозитроии находится сервис на Flask для классификации изображений с помощью нейроннй сети (resnet50)

## Поднятие сервиса

1. Сначала создадим виртуальное окружение:
```
python3 -m venv env
```
2. Активация окружения
```
source env/bin/activate
```
3. Установка зависимости:
```
pip3 install -r requiremets.txt
```
4. Запуск сервиса:
```
python3 app.py
```

## Запросы к сервису
Для настройки хоста и указании файла, который мы хотим классифицировать используется конфигурационный файл [request_config.yaml](https://github.com/Landaunn/service-imagenet/blob/main/request_config.yaml), где можно указать эти параметры <br/>

Далее запускается код запроса:
```
python3 request_example.py
```
Для [картинки](https://github.com/Landaunn/service-imagenet/blob/main/cat.png) из репозитроия ответ сервиса:
```
Egyptian_cat
```
