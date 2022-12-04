from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView

from .models import *

# Create your views here.


# QUERY
def refillingredient(request):
    refillingredient_list = Ingredient.objects.all().filter(quantity_on_hand__lte = 10)
    return render(request, "refillingredient.html", {'ingredient': refillingredient_list})

def orderslip(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    order = Orders.objects.get(customer_id=customer.customer_id)
    shake = Milkshake.objects.all().filter(tx_num = order.tx_num)
    customization = Customization.objects.all()

   #  datadict = {
   #      "customer": customer,
   #      "order" : order,
   #      "shake": shake
   #  }
    
    return render(request, "orderslip.html", {
      "customer": customer,
      "order": order,
      "shakeorders": shake,
      "orders": Orders.objects.all(),
      "shakecustoms": customization
    })

class HomePageView(View):
    def get(self, request):
        customer = Customer.objects.order_by("customer_name")
        return render(request, "index.html", {"customer": customer})



# Compiled View (orders & orderslip)
class OrdersPageView(View):
   def get(self, request):
      return render(request, "blizzardblast.html", {
         "orders": Orders.objects.all()
      })


# dummy just for the button
class OrdersCreateView(CreateView):
   model = Orders
   fields = '__all__'