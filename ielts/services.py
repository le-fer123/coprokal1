from django.http import JsonResponse

from .models import Sample


def get_sample(id):
    return Sample.objects.get_or_404(id=id)


def get_first_part(id_sample):
    sample = Sample.objects.get(id=id_sample)
    first_part = sample.first_part

    return first_part


def get_second_part(id_sample):
    sample = Sample.objects.get(id=id_sample)
    second_part = sample.second_part

    return second_part


def get_third_part(id_sample):
    sample = Sample.objects.get(id=id_sample)
    third_part = sample.third_part

    return third_part


def validation_answer(audio_file, sample_id):
    if not audio_file or not sample_id:
        return JsonResponse({"error": "Both 'audio' and 'sample_id' are required."}, status=400)
