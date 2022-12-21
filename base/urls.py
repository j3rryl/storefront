from django.urls import path
from . import views

#URL conf module
urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"), #dynamics  // name for updating easily
]