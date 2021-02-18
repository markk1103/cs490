from django import forms
from esports_site.models import Posts

class NewPost(forms.ModelForm):
    class Meta:
        model = Posts # the Posts database
        fields = ['title', 'description', 'text'] # fields of the Posts database
