from django.http import HttpResponse


def index(request):
    return HttpResponse('Surprise mazafaka!')


def catalog(request):
    return HttpResponse('Каталог карточек')