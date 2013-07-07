from django.forms import ModelForm
from models import ContactRequests

# Create the form class.
class ContactRequestsForm(ModelForm):
    def __init__(self, *args, **kwargs):            
        super(ContactRequestsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = u'Name'
        self.fields['email'].widget.attrs['placeholder'] = u'Email'
        self.fields['message'].widget.attrs['placeholder'] = u'Message'
    class Meta:
        model = ContactRequests
        fields = ['name', 'email', 'message']