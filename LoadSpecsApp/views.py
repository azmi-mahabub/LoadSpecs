from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render (request, template_name='LoadSpecsHTML\home.html')
