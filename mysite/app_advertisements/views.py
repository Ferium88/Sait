from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Advertisement
from .forms import AdvertisementForm

from django.core.handlers.wsgi import WSGIRequest
def index(request):
    advertisements = Advertisement.objects.all()
    context = {
        "advertisements": advertisements
    }
    return render(request, 'index.html ', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def post_adv(request:WSGIRequest):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            return redirect(
                reverse("index")
            )
    else:
        form = AdvertisementForm()
    context = {
        'form':form
    }
    return render(request, 'advertisement-post.html', context)