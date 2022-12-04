from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.views.generic.edit import CreateView

from .models import *


def refillingredient(request):
    refillingredient_list = Ingredient.objects.all().filter(quantity_on_hand__lte = 10)
    return render(request, "refillingredient.html", {'ingredient': refillingredient_list})


def orderslip(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    order = Orders.objects.get(customer_id=customer.customer_id)
    shake = Milkshake.objects.all().filter(tx_num = order.tx_num)
    customization = Customization.objects.all()

    return render(request, "orderslip.html", {
      "customer": customer,
      "order": order,
      "shakeorders": shake,
      "orders": Orders.objects.all(),
      "shakecustoms": customization
    })


def receipt(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    order = Orders.objects.get(customer_id=customer.customer_id)
    shake = Milkshake.objects.all().filter(tx_num = order.tx_num)
    customization = Customization.objects.all()

    return render(request, "receipt.html", {
      "customer": customer,
      "order": order,
      "shakeorders": shake,
      "orders": Orders.objects.all(),
      "shakecustoms": customization
    })


def newcustomer(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, request.FILES)
        if customer_form.is_valid():
            customer_form.save()
            return redirect("../addorder")
    else:
        customer_form = CustomerForm()
    return render(request, "newcustomer.html", {"customer_form": customer_form})

def neworder(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order_form.save()
            return redirect("../addshake")
    else:
        order_form = OrderForm()
    return render(request, "neworder.html", {"order_form": order_form})

def newshake(request):
    if request.method == "POST":
        shake_form = MilkshakeForm(request.POST, request.FILES)
        if shake_form.is_valid():
            shake_form.save()
            return redirect("../addshake")
    else:
        shake_form = MilkshakeForm()
    return render(request, "newshake.html", {"shake_form": shake_form})

def newingredient(request):
    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST, request.FILES)
        if ingredient_form.is_valid():
            ingredient_form.save()
            return redirect("../orderpreparation")
    else:
        ingredient_form = IngredientForm()
    return render(request, "newingredient.html", {"ingredient_form": ingredient_form})

def newrecipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect("../orderpreparation")
    else:
        recipe_form = RecipeForm()
    return render(request, "newrecipe.html", {"recipe_form": recipe_form})

def newrecipeingredient(request):
    if request.method == "POST":
        recipe_ingredient_form = RecipeIngredientForm(request.POST, request.FILES)
        if recipe_ingredient_form.is_valid():
            recipe_ingredient_form.save()
            return redirect("../orderpreparation")
    else:
        recipe_ingredient_form = RecipeIngredientForm()
    return render(request, "newrecipeingredient.html", {"recipe_ingredient_form": recipe_ingredient_form})

def newcustomization(request):
    if request.method == "POST":
        customization_form = CustomizationForm(request.POST, request.FILES)
        if customization_form.is_valid():
            customization_form.save()
            return redirect("../addcustomization")
    else:
        customization_form = CustomizationForm()
    return render(request, "newcustomization.html", {"customization_form": customization_form})


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