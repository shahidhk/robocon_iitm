# From django mains
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# For dajaxice
from misc.dajaxice.core import dajaxice_functions

# From models
from blog.models import Thread
from sponsors.models import ContactRequests

# From forms
from blog.forms import ThreadForm

# From python
import datetime


def newblog(request):
    '''View for creating a new blog'''
    if request.method == 'POST':
        data = ThreadForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return HttpResponse('<script>alert("Your blog has been submitted succesfully")</script><center>alert(Your blog has been submitted succesfully)</center>')
        else:
            return HttpResponse('<center>Enter valid data</center>')
    else:
        form = ThreadForm()
    return render(request, 'newblog.html', {'form': form})

def blog(request):
    try:
        bloglist = Thread.objects.all()
        num = 0
        thirdone = []
        for i in bloglist:
            # This will truncates the description if it is greater than 100 characters and adds some dots
            i.description = (i.description[:100] + " ....") if len(i.description) > 100 else i.description
            num = num+1
            if num % 3 == 0:
                thirdone.append(num)
        # The above three lines make a list having multiples of 3 upto the total number of posts
        # Required to populate the template having three posts in a row
        return render(request, 'blog.html', {'bloglist': bloglist,'count':thirdone})
    except Exception, e:
        return Http404

def blogpost(request,offset):
    post = Thread.objects.get(pk = offset)
    return render(request, 'blogpost.html', {'post' : post})
