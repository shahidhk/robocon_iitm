# For simple dajax(ice) functionalities
from django.utils import simplejson
from misc.dajaxice.decorators import dajaxice_register
from misc.dajax.core import Dajax
from misc.dajaxice.utils import deserialize_form
# For rendering templates
from django.template import RequestContext
from django.template.loader import render_to_string
# From views
# From forms
from sponsors.forms import ContactRequestsForm
# From models
from sponsors.models import ContactRequests
# From Misc
from misc.utilities import show_alert

@dajaxice_register(method="GET", name="misc.hello_get")
@dajaxice_register(method="POST", name="misc.hello_post")
def hello(request, form=None):
    """
        Test dajax
    """
    dajax = Dajax()
    
    dajax.alert("got from dajax");
    
    return dajax.json()

@dajaxice_register(method="GET", name="home.contactus_get")
@dajaxice_register(method="POST", name="home.contactus_post")
def contactus(request, form = None):
    """
        Handles the "contact us" form on the home page
    """
    dajax = Dajax() # to hold dajax-json
    
    if request.method == 'POST':
        form = ContactRequestsForm(deserialize_form(form))
        print form
        if form.is_valid(): # check validity
            form.save()
            # @Ali: clear the form after saving it, the below command didnt do it, and make the send button pseud
            #form = ContactRequestsForm()
            show_alert(dajax, "success", "Your message has been submitted. We will get back to you shortly")
        else: # form was not valid, show errors
            dajax.remove_css_class('#form_footer_contactus input', 'error')
            for error in form.errors: # tell which parts had errors
                dajax.add_css_class('#id_%s' % error, 'error')
            print [error for error in form.errors]
            show_alert(dajax, 'error', "There were some errors : please rectify them") # show alert
    else: # GET - nothing to do
        pass
    
    return dajax.json()
