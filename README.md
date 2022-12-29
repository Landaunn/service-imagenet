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

Также модель сейчас равёрнута по адресу http://93.175.9.182:8900/predict <br/>
К ней можно обратиться либо способом выше с указанием в конфиге 'host: "93.175.9.182"' и 'port: "8900"', либо через curl запрос <br/>
Пример curl запроса:
```
!curl \
-F 'file=@/path/to/image/image.png;type=image/png' \
-X POST \
http://93.175.9.182:8900/predict
```
