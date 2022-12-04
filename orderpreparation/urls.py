from django.urls import path
from .views import *

app_name = 'orderpreparation'
urlpatterns = [
    path("orderpreparation/", HomePageView.as_view(), name='index'),
    path("refillingredient/", refillingredient, name = 'refillingredient'),
   #  path("orderpreparation/<int:customer_id>/", orderslip,),


    path("orders/", OrdersPageView.as_view(), name='blizzardblast'),
    path("orders/<int:customer_id>/", orderslip, name='orderslip'),
    path("orders/add/", OrdersCreateView.as_view(), name='new-order'),
    path("orders/<int:customer_id>/receipt/", receipt, name='receipt'),
]