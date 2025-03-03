from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<str:room_id>/', views.room, name='room'),  # Direct room access
    path('checkhome', views.checkhome, name='checkhome'),
    path('createRoom', views.createRoom, name='createRoom'),
    path('CreateNewRoom', views.CreateNewRoom, name='CreateNewRoom'),
    
]
