from django.template import loader
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Bb

# Create your views here.
# option for render
def index(request):
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    
    return render(request, 'bboard/index.html', context=context)

'''
option1 with loader
def index(request):
    template    = loader.get_template('bboard/index.html')
    bbs         = Bb.objects.order_by('-published')
    context     = {
        'bbs': bbs,
    }
        
    return HttpResponse(template.render(context, request))
'''

