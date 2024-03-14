from django.urls import path, re_path

from . import views

app_name = 'canchas_app'

urlpatterns = [
    path('api/canchas/list', views.CanchaList.as_view(), name='canchas'),
]
