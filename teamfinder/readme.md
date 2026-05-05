# TeamFinder

**TeamFinder** — это веб-приложение для поиска команды и совместной работы над проектами.
Пользователи могут создавать проекты, присоединяться к другим участникам, а также сохранять интересные проекты в избранное.

---

## Функциональность

* Регистрация и авторизация пользователей (по email)
* Создание, редактирование и завершение проектов
* Участие в проектах других пользователей
* Добавление проектов в избранное
* Просмотр профилей пользователей
* Фильтрация пользователей по различным критериям

---

## Стек технологий

* Python 3
* Django
* PostgreSQL
* Docker / Docker Compose
* HTML / CSS (Django Templates)

---

## Запуск проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/MiroslavaZh/team-finder-ad.git
cd teamfinder
```

### 2. Создание файла `.env`

Создайте файл `.env` в корне проекта и заполните его:

```env
DEBUG=True
SECRET_KEY=your_secret_key

DB_NAME=teamfinder
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### 3. Запуск через Docker

```bash
docker compose up -d --build
```

### 4. Применение миграций

```bash
docker compose exec web python manage.py migrate
```

### 5. Создание суперпользователя (опционально)

```bash
docker compose exec web python manage.py createsuperuser
```

### 6. Запуск проекта

```bash
docker compose exec web python manage.py runserver 0.0.0.0:8000
```

Приложение будет доступно по адресу:
http://localhost:8000

---

## Структура проекта

* `users` — приложение пользователей (кастомная модель пользователя)
* `projects` — приложение проектов
* `templates_var1` — HTML-шаблоны
* `static` — статические файлы
* `media` — пользовательские файлы

---

## Автор

* Жиздюк Мирослава

## Для ревью

# Создайте файл `.env` в корне проекта и заполните его:

```env
DEBUG=True
SECRET_KEY=your_secret_key

DB_NAME=teamfinder
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

# Перейти в корень проекта:

```bash
cd teamfinder
```

# Запустить проект:

```bash
docker compose up --build
```

# Применить миграции:

```bash
docker compose exec web python manage.py migrate
```

# Загрузить тестовые данные:

```bash
docker compose exec web python manage.py seed_data
```

После этого проект доступен по адресу:

http://localhost:8000

# Тестовые пользователи

user1

email: user1@test.com
password: 12345678

user2

email: user2@test.com
password: 12345678

user3

email: user3@test.com
password: 12345678