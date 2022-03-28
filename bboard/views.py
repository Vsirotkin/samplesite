from django.template import loader
from django.http.response import HttpResponse
from .models import Bb

# Create your views here.
def index(request):
    template    = loader.get_template('bboard/index.html')
    bbs         = Bb.objects.order_by('-published')
    context     = {
        'bbs': bbs,
    }
        
    return HttpResponse(template.render(context, request))
