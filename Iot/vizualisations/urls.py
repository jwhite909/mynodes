from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:vizualisation_id>/', views.view, name='view')
]