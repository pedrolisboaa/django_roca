from django.urls import path
from .views import index, cadastro, contato

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('contato/', contato, name='contato'),
]
