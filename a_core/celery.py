import os
from celery import Celery

# Set the default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

app = Celery('a_core')

# Load task modules from all registered Django app configs
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks from installed Django apps
app.autodiscover_tasks()

# Optional: Debugging print statement
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Celery Beat schedule for periodic tasks
app.conf.beat_schedule = {
    'run-every-10-seconds': {
        'task': 'a_home.tasks.check_status_for_all_users',  # Replace 'app_name' with your actual app name
        'schedule': 10.0,  # Run every 10 seconds
    },
}
