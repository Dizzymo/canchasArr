from django.urls import path
from . import views
from .views import LoginAPIView
from rest_framework.documentation import include_docs_urls
app_name = 'usuarios_app'

urlpatterns = [
    #cliente
    path('login/', views.LoginView.as_view(), name = "login"),
    path('api/usuarios/login/', views.LoginAPIView.as_view(), name = "api_login"),
    
    
]