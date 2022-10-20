from django import forms
from .models import SubscribedUsers

class NewsletterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput, required=True)
    
    class Meta:
        model = SubscribedUsers
        fields = "__all__"
        