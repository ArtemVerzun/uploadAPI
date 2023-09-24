from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        document_serializer = FileSerializer(data=request.data)
        if document_serializer.is_valid():
            file_obj = document_serializer.save()
            # Здесь обрабатываем файл асинхронно с использованием Celery
            process_file.delay(file_obj.id)
            return Response(document_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(APIView):
    def get(self, request):
        files = File.objects.all()
        file_serializer = FileSerializer(files, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)
