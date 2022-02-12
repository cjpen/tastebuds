
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('groups/', views.groups_index, name='index'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
]
