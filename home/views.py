# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.models import User

def main(request):
    pageTitle = "This is CSPCLAB's Home :)"
    menuDictionary = { 
            "Home":"home",
            };
    tpl = loader.get_template('main.html')
    ctx = Context({
        'user':request.user,
        'pageTitle':pageTitle,
        'menuDictionary':menuDictionary,
        })
    return HttpResponse( tpl.render( ctx ) )
