# Django Task Management API

## Описание проекта

Этот проект представляет собой API для управления задачами с использованием Django и Django REST Framework. API позволяет создавать задачи, а также получать список всех задач. Проект включает в себя:

- Роуты для получения списка задач и создания новой задачи.
- Валидацию данных для поля `title` задачи.
- Документацию API через Swagger и Redoc.

## Установка и запуск проекта

### Требования

1. Python 3.8+
2. Django 4.x, 5.x
3. Django REST Framework
4. drf_yasg для генерации документации Swagger и Redoc

### Шаги для запуска

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Vkalaitanov/TZ_proj.git
    cd TZ_proj
    ```

2. Создайте и активируйте виртуальное окружение:

    Для Linux/MacOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Для Windows:
    ```bash
    python3 -m venv venv
    venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции:

    ```bash
    python manage.py migrate
    ```

5. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

6. Откройте API в браузере:

    - Админ-панель: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
    - Документация API (Swagger): [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
    - Документация API (Redoc): [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Пример запроса

### 1. Создать задачу (POST)

Для создания новой задачи отправьте POST запрос на эндпоинт `/tasks/`:

**URL:** `http://127.0.0.1:8000/tasks/`

**Тело запроса:**
```json
{
    "title": "Новая задача",
    "is_completed": false
}
```


### Получить список задач (GET)

Для получения списка всех задач сделайте GET запрос:

**URL:** `http://127.0.0.1:8000/tasks/`

**Ответ:**
```json
[
    {
        "id": 1,
        "title": "Задача 1",
        "is_completed": false
    }
]

