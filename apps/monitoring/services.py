from django.core.cache import cache
from .tasks import send_welcome_email_task
def get_stats():
    cache_key = "monitoring:stats:v1"
    stats = cache.get(cache_key)
    if stats is None:
        stats = {"users_count": 1000, "active_orders": 42}
        cache.set(cache_key, stats, timeout=60)
    return stats
def register_user(email):
    task = send_welcome_email_task.delay(email)
    return {"message": "Registration accepted", "email": email, "task_id": task.id}
