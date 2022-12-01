from django.contrib import admin

from .models import Customer, Customization, Employee, Ingredient, Manager, Milkshake, Orders, Recipe, RecipeIngredient, Staff

admin.site.register(Customer)
admin.site.register(Customization)
admin.site.register(Employee)
admin.site.register(Ingredient) 
admin.site.register(Manager)
admin.site.register(Milkshake)
admin.site.register(Orders) 
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Staff)