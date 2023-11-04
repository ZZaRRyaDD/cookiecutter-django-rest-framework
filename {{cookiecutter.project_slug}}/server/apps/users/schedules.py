from celery import schedules

from config.celery import app

app.conf.beat_schedule = {
   'user_count': {
        'task': 'apps.users.tasks.user_count',
        'schedule': schedules.crontab(),
   },
}
