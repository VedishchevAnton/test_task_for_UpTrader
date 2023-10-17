# Тестовое задание для компании UpTrader

### Задание
#### Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД

#### Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
#### {% draw_menu 'main_menu' %}
#### При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.


### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/VedishchevAnton/test_task_for_UpTrader.git
cd task_for_UpTrader
```

#### Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```


#### Обновляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate --noinput
```

#### Создайте суперпользователя Django:
```bash
python manage.py createsuperuser
```

#### Запускаем сервер:
```bash
python manage.py runserver
```

#### Админка доступна по ссылке  http://localhost:8000/admin/ 