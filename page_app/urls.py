from django.urls import path
from page_app.views import index, services

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),
    path('services', services),
]