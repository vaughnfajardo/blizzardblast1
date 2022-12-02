from django.urls import path
from . import views

app_name = 'orderpreparation'
urlpatterns = [
    path("", views.HomePageView.as_view(), name='index'),
    path("orderpreparation/<int:customer_id>", views.orderpreparation, name='orderpreparation'),
]