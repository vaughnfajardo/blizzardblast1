from django.urls import path
from .views import *

app_name = 'orderpreparation'
urlpatterns = [
    path("orderpreparation/", HomePageView.as_view(), name='index'),
    path("refillingredient/", refillingredient, name = 'refillingredient'),
    path("orderpreparation/<int:customer_id>/", orderslip, name='orderslip'),
    path('addcustomer/', newcustomer, name='addcustomer'),
    path('addorder/', neworder, name='addorder'),
    path('addshake/', newshake, name='addshake'),
    path('addingredient/', newingredient, name='addingredient'),
    path('addrecipe/', newrecipe, name='addrecipe'),
    path('addrecipeingredient/', newrecipeingredient, name='addrecipeingredient'),
    path('addcustomization/', newcustomization, name='addcustomization'),
]