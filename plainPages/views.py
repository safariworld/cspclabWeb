# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from cspclabWeb.forms import *

def aboutUs(request):
    var = RequestContext(request,{
        'head_title':'About Us',})
    
    return render_to_response(
            'aboutUs.html',
            var,
    )
   
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email']
            )
            group = Group.objects.get(name='guest')
            group.user_set.add(user)
            return HttpResponseRedirect('/plain/accounts/register_success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request,{
        'form':form
    })
    return render_to_response(
        'registration/signup.html',
        variables
    )

def achievements(request):
    
    var = RequestContext(request,{

    })
    return render_to_response(
            'achievements.html',
            var,
    )

def calendar(request):
    
    var = RequestContext(request,{

        })
    return render_to_response(
            'calendar.html',
            var,
    )

def profile(request):

    var = RequestContext(request,{

        })
    return render_to_response(
            'profile.html',
            var
            )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
