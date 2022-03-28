from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Bb

# Create your views here.
def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += f'{bb.title} "\r\n" {bb.content} "\r\n\r\n"'
        
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
