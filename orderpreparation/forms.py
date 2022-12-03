from django.forms import forms, ModelForm
from .models import *


#Forms for creating Customers and their Orders.
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class MilkshakeForm(ModelForm):
    class Meta:
        model = Milkshake
        fields = '__all__'


#Forms to create new Recipes, Customizations, Ingredients, etc.

class RecipeForm:
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeIngredientForm:
     class Meta:
        model = Recipe
        fields = '__all__'

class IngredientForm:
    class Meta:
        model = Ingredient
        fields = '__all__'

class CustomizationForm:
    class Meta:
        model = Customization
        fields = '__all__'
