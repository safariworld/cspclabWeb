# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
#from cspclabWeb.forms import *

def aboutUs(request):
    template = get_template('aboutUs.html')	
    var = Context({
        'head_title': 'About Us',
    })
    return HttpResponse( template.render(var) )
"""
def register(request):
    if request.method == 'post':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    username=form.cleaned_data['username']
                    password=form.cleaned_data['password1']
                    email=form.cleaned_data['email']
                    mobile=form.cleaned_data['mobile']
                    )
            return HttpResponseRedirect('plain/account/register_success/'))
        else:
            form = RegistrationForm()

        variables = RequestContext(request,{
            'form':form
        })
        return render_to_response(
                'registration/signup.html',
                variables
        )
"""
def achievements(request):
    template = get_template('achievements.html')
    var = Context({
    })
    return HttpResponse( template.render(var) )

def calendar(request):
    template = get_template('calendar.html')
    var = Context({
        })
    return HttpResponse( template.render(var) )
