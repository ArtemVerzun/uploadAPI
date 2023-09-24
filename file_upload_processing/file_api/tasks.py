from celery import shared_task
from .models import File


@shared_task
def process_file(file_id):
    file_obj = File.objects.get(id=file_id)
    # Здесь выполняем обработку файла
    # После обработки файла изменяем поле processed на True
    file_obj.processed = True
    file_obj.save()
