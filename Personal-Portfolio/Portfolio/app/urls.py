from django.urls import path
from . import views

urlpatterns = [
    path("",views.Index,name='index'),
    path("contact/",views.ContactUs,name="contact"),

]