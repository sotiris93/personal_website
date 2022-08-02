from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('create/', views.create),
    path('update/<int:pk>/', views.update),
    path('<int:pk>/delete/', views.delete),
]
