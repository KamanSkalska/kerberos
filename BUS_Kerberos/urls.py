from django.urls import path, include


urlpatterns = [
    path("", include("KDC.urls")),
    path("client/", include("Client.urls")),

]
