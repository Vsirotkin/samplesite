from django.template import loader
from django.shortcuts import render
#from django.http.response import HttpResponse
from .models import Bb, Rubric

# Create your views here.
# option for render
def index(request):
    bbs     = Bb.objects.all()
    rubrics = Rubric.objects.all()
    
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
    }
    
    return render(request, 'bboard/index.html', context=context)


def by_rubric(request, rubric_id):
    bbs             = Bb.objects.filter(rubric=rubric_id)
    rubrics         = Rubric.objects.all()
    current_rubric  = Rubric.objects.get(pk=rubric_id)
    
    context         = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric}
    
    return render(request, 'bboard/by_rubric.html', context=context)

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
