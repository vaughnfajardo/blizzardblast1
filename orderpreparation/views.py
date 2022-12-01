from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View

from .models import *

# Create your views here.

def orderpreparation(request):
    order_list = Orders.objects.all()
    milkshake_list = Milkshake.objects.all()
    customizations_list = Customization.objects.all()
    return render(request, 'orderpreparation.html', 
    {"order_list": order_list, "milkshake_list":milkshake_list, "customizations_list":customizations_list})
