# Контрольная работа: Redis + Celery + Docker Compose

## Запуск (Windows PowerShell)

1. Убедитесь, что Docker Desktop запущен. В архив уже включён `.env` для локального запуска.
2. При необходимости измените `SECRET_KEY` и пароль PostgreSQL в `.env`. Не используйте эти значения в production.
3. Из корня проекта выполните `docker compose up --build`.

Docker Compose поднимает пять сервисов: `web`, `db`, `redis`, `celery_worker`, `celery_beat`.

## Проверка API

Статистика с кэшированием на 60 секунд:

```bash
curl http://localhost:8000/api/v1/stats/
```

Асинхронная имитация отправки письма:

```bash
curl -X POST http://localhost:8000/api/v1/register/ -H "Content-Type: application/json" -d '{"email":"test@example.com"}'
```

Worker и Beat логи:

```bash
docker compose logs -f celery_worker
docker compose logs -f celery_beat
```

Тесты API (в контейнере web):

```bash
docker compose exec web python manage.py test apps.monitoring.tests
```

Остановка: `docker compose down`. Для удаления также хранимого тома БД используйте `docker compose down -v` (данные PostgreSQL будут удалены).

## Архитектура

- `views.py`: HTTP/API слой.
- `serializers.py`: проверка входящего email.
- `services.py`: бизнес-логика и вызов фоновой задачи.
- `selectors.py`: зарезервированный read/query слой для будущих выборок.
- `tasks.py`: задачи Celery.
- `core/celery.py`: настройка Celery.
