from django.urls import path
from .views import *

app_name = 'orderpreparation'
urlpatterns = [
    path("orderpreparation/", HomePageView.as_view(), name='index'),
    path("refillingredient/", refillingredient, name = 'refillingredient'),
    path("orderpreparation/<int:customer_id>/", orderslip, name='orderslip'),
]