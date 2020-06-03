from django.urls import path
from core import views

urlpatterns = [
    path('', views.hello_world, name="hello_world"),
]