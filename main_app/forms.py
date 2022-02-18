from django.forms import ModelForm
from .models import Event, Profile, Recipe

class EventForm(ModelForm):
  required_css_class = 'required-field'
  class Meta:
    model = Event
    fields = ['title', 'host', 'location', 'datetime']

class ProfileForm(ModelForm):
  required_css_class = 'required-field'
  class Meta:
    model = Profile
    fields = ['name']

class RecipeForm(ModelForm):
  required_css_class = 'required-field'
  class Meta:
    model = Recipe
    fields = ['title', 'url']