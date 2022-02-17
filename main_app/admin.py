from django.contrib import admin
from .models import Group, Event, Profile, Recipe, Vote, PhotoGroup, PhotoEvent, PhotoProfile, PhotoRecipe

# Register your models here.
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Recipe)
admin.site.register(Vote)
admin.site.register(PhotoGroup)
admin.site.register(PhotoEvent)
admin.site.register(PhotoProfile)
admin.site.register(PhotoRecipe)
