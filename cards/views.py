from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


def index(request):
    return render(request, 'cards/main.html')


def about(request):
    return render(request, 'cards/about.html')


def catalog(request):
    return render(request, 'cards/catalog.html')


def get_categories(request):
    return HttpResponse('All categories')


def get_cards_by_category(request, slug):
    return HttpResponse(f'Cards by category {slug}')


def get_cards_by_tag(request, slug):
    return HttpResponse(f'Cards by tag {slug}')


def get_detail_card_by_id(request, card_id):
    return HttpResponse(f'Detail card by id {card_id}')
