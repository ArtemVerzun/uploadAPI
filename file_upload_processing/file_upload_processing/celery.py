import os
import celery

# Устанавливаем переменную окружения для указания на файл настроек Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_upload_processing.settings')

app = celery.Celery('file_upload_processing')

# Загружаем настройки из файла настроек проекта
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач в приложениях Django
app.autodiscover_tasks()

