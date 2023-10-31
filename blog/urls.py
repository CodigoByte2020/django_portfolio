from django.urls import path
from . import views

app_name = 'blog'  # PARA PODER LLAMAR A LAS RUTAS PERTENECIENTES A ESTE MÓDULO

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
]