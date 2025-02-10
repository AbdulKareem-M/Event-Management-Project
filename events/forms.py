from django import forms
from .models import EventModel

class EventForm(forms.ModelForm):
  class Meta:
    model =EventModel
    fields = '__all__'
    
    