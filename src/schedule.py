from celery.schedules import crontab
from src.tasks import app

app.conf.beat_schedule = {
    "get-images-task-120-min": {
        "task": "src.tasks.get_images",
        "schedule": crontab(hour=2, day_of_week=6),
    }
}
app.conf.timezone = "UTC"
