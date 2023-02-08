from django.http.response import HttpResponse

from .models import TestModel


def test(request):
    test_records = TestModel.objects.using(request.using_db).all()
    result = []
    for test in test_records:
        result.append({'id': test.id, 'name': test.name})
    return HttpResponse(result)
