from django.http import HttpResponse, Http404
import datetime
def home(request):
	now=datetime.datetime.now()
	html="<center><h1>Home page<br/></h1>Its %s now</center>" % now
	return HttpResponse(html)