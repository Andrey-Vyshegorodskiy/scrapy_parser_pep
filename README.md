# Aсинхронный парсер PEP
Парсер документов PEP на базе фреймворка Scrapy. Парсер создает два файла отчета: файл со списком PEP, включающим номер документа, название и статус и файл суммарной статистики по количеству документов в разных статусах. Это учебный проект

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Над проектом работали](#над-проектом-работали)

## Технологии
- [Python](https://www.python.org/)
- [Scrapy](https://scrapy.org/)

## Использование
1. Клонировать репозиторий к себе на компьютер:

```bash
git clone git@github.com:sniki-ld/scrapy_parser_pep.git
```
2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```
3. Установить зависимости из файла requirements.txt, который лежит в корне проекта:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
___

## Запуск парсера:
```
scrapy crawl pep
```
___
## Результаты работы парсера:
Парсер выводит собранную информацию в два файла .csv:
- В первом файле (именован по маске `pep_ДатаВремя.csv`) - список всех PEP: номер, название и статус.
  

- Во втором файле (именован по маске `statussummaryДатаВремя.csv`) содержится сводка по статусам PEP — 
  сколько найдено документов в каждом статусе (статус, количество) и общее количество всех документов.

## Над проектом работали

- Андрей Вышегородский
