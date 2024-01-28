# Інструкції для локального запуску проєкту:

1) Клонуйте репозиторій backend-labs
```bash
$ git clone https://github.com/ShynHlib/backend-labs
$ cd backend-labs
```
3) Локально ініціалізувати змінні середовища DB_USER, DB_PASSWORD, DB_HOST, DB_NAME(значення вказані для прикладу):
```bash
$ export DB_USER=user
$ export DB_PASSWORD=password
$ export DB_HOST=host
$ export DB_NAME=name
```
Для Windows використовуйте команду ```set```.

3) Запустіть докер
4) Скомпілюйте та запустіть контейнер
```bash
$ docker-compose build
$ docker-compose up
```
# Варіант завдання 3-ої лабораторної:
26 % 3 = 2

**Користувацькі категорії витрат** - повинні бути загальні категорії витрат, які видно всім користувачам, та користувацькі, які можуть вказати тільки користувачі, які їх визначили.
