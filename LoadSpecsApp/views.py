from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, template_name="LoadSpecsHTML/home.html")

def profile(request):
    return render (request, template_name="LoadSpecsHTML/profile.html")

def tasks(request):
    return render (request, template_name="LoadSpecsHTML/tasks.html")

def team(request):
    return render (request, template_name="LoadSpecsHTML/team.html")