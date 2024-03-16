from django.urls import path
from . import views

app_name = 'usuarios_app'

urlpatterns = [
    #cliente
    path('login/', views.LoginView.as_view(), name = "login"),
     
]