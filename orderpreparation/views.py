from django.shortcuts import render, redirect
from django.views import View
from .forms import *
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

    datadict = {
        "customer": customer,
        "order" : order,
        "shake": shake
    }
    
    return render(request, "orderslip.html", datadict)

class HomePageView(View):
    def get(self, request):
        customer = Customer.objects.order_by("customer_name")
        return render(request, "index.html", {"customer": customer})

#forms views

def newcustomer(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, request.FILES)
        if customer_form.is_valid():
            customer_form.save()
            return redirect("../orderpreparation")
    else:
        customer_form = CustomerForm()
    return render(request, "newcustomer.html", {"customer_form": customer_form})

def neworder(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order_form.save()
            return redirect("../orderpreparation")
    else:
        order_form = OrderForm()
    return render(request, "neworder.html", {"order_form": order_form})

def newshake(request):
    if request.method == "POST":
        shake_form = MilkshakeForm(request.POST, request.FILES)
        if shake_form.is_valid():
            shake_form.save()
            return redirect("../orderpreparation")
    else:
        shake_form = MilkshakeForm()
    return render(request, "newshake.html", {"shake_form": shake_form})




