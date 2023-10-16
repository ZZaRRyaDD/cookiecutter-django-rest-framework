from config.celery import app, schedules

app.conf.beat_schedule = {
   'user_count': {
        'task': 'apps.users.tasks.user_count',
        'schedule': schedules.crontab(),
   },
}
