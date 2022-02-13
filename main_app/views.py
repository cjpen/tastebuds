from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Group

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard (request):
    return render(request, 'dashboard.html')

def groups_index(request):
    groups = Group.objects.all()
    return render(request, 'groups/index.html', {'groups': groups})

def groups_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    return render(request, 'groups/detail.html',{'group': group})

# Class-Based View (CBV)
class GroupCreate(LoginRequiredMixin, CreateView):
  model = Group
  fields = ['name', 'leader_username', 'description']

  # This inherited method is called when a
  # valid group form is being submitted
  def form_valid(self, form):
    # form.instance is the group object
    form.instance.user = self.request.user
    return super().form_valid(form)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect ('dashboard')
    else:
      error_message = 'Invalid Sing Up, Try Again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

