from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("main/",views.main_page,name="main"),
    #path('receive-message/', views.receive_message, name='receive_message'),
    path('login/', views.login_form, name ='login'),
    path('register/', views.registering_form, name ='register'),
    path("service/",views.service,name="service")
]