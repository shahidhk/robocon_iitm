# For simple dajax(ice) functionalities
from django.utils import simplejson
from misc.dajaxice.decorators import dajaxice_register
from misc.dajax.core import Dajax
from misc.dajaxice.utils import deserialize_form
# For rendering templates
from django.template import RequestContext
from django.template.loader import render_to_string
# Decorators
from django.contrib.auth.decorators import login_required
# From views
# From forms
from blog.forms import ThreadForm
# From models
from sponsors.models import ContactRequests
from blog.models import Thread
# From Misc
from misc.utilities import show_alert

@dajaxice_register(method="GET", name="blog.show")
@dajaxice_register(method="POST", name="blog.show")
def show_blog(request, primkey = None):
    """
        Shows the blog entries on the page
        
        Populates : Features
        
        Removes : Showcase, Sponsors
    """
    dajax = Dajax()
    
    dajax.add_css_class('#showcase', 'hide')
    dajax.add_css_class('#sponsors', 'hide')
    
    html_content = ""
    
    if primkey:
        pass
        show_alert(dajax, "info", "This part has not yet been completed")
    else:
        bloglist = Thread.objects.all()
        #print bloglist
        for i in bloglist:
            i.description = (i.description[:100] + " ....") if len(i.description) > 100 else i.description
        html_content = render_to_string('blog/show.html', {'bloglist': bloglist}, RequestContext(request))
        
    if html_content:
        dajax.assign('#features', 'innerHTML', html_content);
    
    return dajax.json()


@dajaxice_register(method="GET", name="blog.new_get")
@dajaxice_register(method="POST", name="blog.new_post")
def new_blog(request, form = None):
    """
        Handles the creation of a blog post
        - if user not logged in, give alert
        
        Populates : Features
        
        Removes : Showcase, Sponsors
    """
    dajax = Dajax()
    
    html_content = ""
    dajax.add_css_class('#showcase', 'hide')
    dajax.add_css_class('#sponsors', 'hide')
    
    if request.method == 'POST':
        form = ThreadForm(deserialize_form(form))
        print form
        if form.is_valid(): # check validity
            form.save()
            show_alert(dajax, "success", "Your post has been saved !")
        else: # form was not valid, show errors
            dajax.remove_css_class('#form_new_blog_post input', 'error')
            for error in form.errors: # tell which parts had errors
                dajax.add_css_class('#id_%s' % error, 'error')
            print [error for error in form.errors]
            show_alert(dajax, 'error', "There were some errors : please rectify them") # show alert
    else: # GET - display empty form
        form = ThreadForm()
        html_content = render_to_string('blog/new.html', {'form': form}, RequestContext(request))
    
    if html_content:
        dajax.assign("#features", "innerHTML", html_content)
    
    return dajax.json()
