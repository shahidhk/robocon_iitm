# From django main
from django import forms

# From models
from blog.models import Thread

class Blog(forms.ModelForm):
    class Meta:
        model = Thread
        fields=['title','author','pic','description']
