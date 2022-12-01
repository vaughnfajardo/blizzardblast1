from django.urls import path
from . import views

app_name = 'orderpreparation'
urlpatterns = [
    path('orderpreparation/', views.orderpreparation, name='orderpreparation'),
]