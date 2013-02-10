# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def aboutUsView(request):
	template = get_template('aboutUs.html')	
	var = Context({
		'head_title': 'About Us',
	})
	return HttpResponse( template.render(var) )
