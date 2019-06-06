# sendemail/forms.py
from django import forms
from .models import UsersRatings

class ContactForm(forms.Form):
    your_email_address = forms.EmailField(required=True)
    your_name = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    Enter_a_plus_sign_to__help_prove_you_are_not_a_robot = forms.CharField(required=True)


class RatingsForm(forms.ModelForm):
    class Meta:
        model = UsersRatings
        fields = [
            'general',
            'car',
            'golf', 
            'house',
            'morning'
            ]




    
    