
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('groups/', views.groups_index, name='index'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('groups/<int:group_id>/', views.groups_detail, name='detail'),

    path('events/<int:group_id>/create/', views.events_create, name='events_create'),
    path('groups/<int:group_id>/add_event/', views.add_event, name='add_event'),
    # path('groups/<int:pk>/events_create/', views.EventCreate.as_view(), name='events_create'),
    # path('groups/<int:group_id>/events/<int:event_id>', views.EventCreate.as_view(), name='events_detail'),
]
