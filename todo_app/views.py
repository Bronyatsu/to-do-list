from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Owner, Patient
from .forms import OwnerCreateForm, PatientCreateForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
