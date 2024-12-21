from rest_framework import viewsets
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import os
from .serializers import *
from .services import *


class AnswerUploadView(View):
    def post(self, request, *args, **kwargs):
        audio_file = request.FILES.get('audio')
        sample_id = request.POST.get('sample_id')
        validation_answer(audio_file, sample_id)

        try:
            sample = get_sample(sample_id)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Sample with this ID does not exist."}, status=404)

        # Сохраняем аудиофайл
        audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', audio_file.name)
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        with open(audio_path, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)

        # Логика обработки (например, связать аудио с Sample или выполнить что-то еще)
        # Пример: sample.audio_path = 'audio/' + audio_file.name
        # sample.save()

        return JsonResponse({"message": "Audio uploaded successfully", "sample_id": sample.id})


class FirstPartViewSet(viewsets.ModelViewSet):
    queryset = FirstPart.objects.all()
    serializer_class = FirstPartSerializer
class SecondPartViewSet(viewsets.ModelViewSet):
    queryset = FirstPart.objects.all()
    serializer_class = FirstPartSerializer
class ThirdPartViewSet(viewsets.ModelViewSet):
    queryset = ThirdPart.objects.all()
    serializer_class = ThirdPartSerializer

class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = IELTSSampleSerializer



