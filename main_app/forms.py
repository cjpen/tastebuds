from django.forms import ModelForm
from .models import Event, Profile

class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['title', 'host', 'location', 'datetime']

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['name']
