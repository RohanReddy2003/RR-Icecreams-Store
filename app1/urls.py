from django.urls import path
from . import views

urlpatterns = [
    path("",views.loginUser,name ='login'),
    path("home",views.home,name ='home'),
    path("about",views.about,name ='about'),
    path("services",views.services,name ='services'),
    path("contact",views.contact,name ='contact'),
    path("login",views.loginUser,name ='login'),
    path("logout",views.logoutUser,name ='logout'),

    # path("submitcontact",views.contact,name ='contact'),
]
