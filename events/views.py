from django.shortcuts import render
from .models import Events, Mainbanner

# Create your views here.
def index(request):
    evnts = Events.objects.all()
    mains = Mainbanner.objects.all()
    return render(request,"index.html", {'evnts' : evnts, 'mains' : mains })

    