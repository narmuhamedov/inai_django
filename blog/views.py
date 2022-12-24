from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1>Страница обо мне </h1>")


def posts(request):
    post = models.Poster.objects.all()
    return render(request, "post.html", {"post_object": post})


# For about us
def about(request):
    about = models.About_us.objects.all()
    return render(request, "about.html", {"about": about})


# For contacts
def contacs(request):
    contact = models.Contacts.objects.all()
    return render(request, "contacts.html", {"concatct": contact})


# For Firma
def firma(request):
    firms = models.Firma.objects.all()
    return render(request, "firma.html", {"firms": firms})
