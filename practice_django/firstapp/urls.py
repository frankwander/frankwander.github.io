from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wander", views.wander, name="wander"), 
    path("david", views.david, name="david"),
    path("<str:name>", views.greet, name="greet")
]