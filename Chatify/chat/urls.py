from django.urls import path
from . import views

urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),
    path('add_message/', views.add_message, name='add_message'),
    path('', views.index, name='index'),  # Uncomment if you have an index view
]
