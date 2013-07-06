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
# From models
# From Misc

@dajaxice_register(method="GET", name="misc.hello_get")
@dajaxice_register(method="POST", name="misc.hello_post")
def hello(request, form=None):
    """
        Test dajax
    """
    dajax = Dajax()
    
    dajax.alert("got from dajax");
    
    return dajax.json()
