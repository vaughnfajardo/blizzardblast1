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
   #  path("orderpreparation/<int:customer_id>/", orderslip,),


    path("orders/", OrdersPageView.as_view(), name='blizzardblast'),
    path("orders/<int:customer_id>/", orderslip, name='orderslip'),
    path("orders/add/", OrdersCreateView.as_view(), name='new-order'),
    path("orders/<int:customer_id>/receipt/", receipt, name='receipt'),
]