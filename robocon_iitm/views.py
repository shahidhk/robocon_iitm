from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from models import ContactRequests, Thread
from forms import Blog
import datetime

def test(request):
    now=datetime.datetime.now()
    html = " <center><h1>Home page<br/></h1>Its %s now</center> " % now
    return HttpResponse(html)
    
def home(request):
	if request.method ==  'POST':
		data=request.POST.copy()
		contact=ContactRequests.objects.create(name=data['name'],timestamp=data['timestamp'],pic=data['pic'],email=data['email'],message=data['message'])
		contact.save()
		return HttpResponse('<center>Your request has been submitted succesfully</center>')
	else:
		return render_to_response ('base.html', {}, context_instance=RequestContext(request))

def newblog(request):
	'''View for creating a new blog'''
	if request.method == 'POST':
		'''
		data=request.POST.copy()
		files=request.FILES.copy()
		blogdata=Thread.objects.create(title=data['title'],subject=data['subject'],pic=files['pic'],description=data['description'])
		blogdata.save()
		'''
		the_model= Blog(request.POST, request.FILES)
		if the_model.is_valid():
			data=the_model.cleaned_data
			print 'valid'
			print data['title']
			return HttpResponse('<center>Your blog has been submitted succesfully</center>')

		else:
			print "not valid"
			return HttpResponse('<center>Enter valid data</center>')

	else:
		form=Blog()
	return render(request, 'blog.html', {'form': form})

def template(request):
    return render_to_response ('template.html', {}, context_instance=RequestContext(request))
    
def blur(request):
    return render_to_response ('blur.html', {}, context_instance=RequestContext(request))
