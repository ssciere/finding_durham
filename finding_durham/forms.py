# sendemail/forms.py
from django import forms
from .models import UsersRatings

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




    
    
