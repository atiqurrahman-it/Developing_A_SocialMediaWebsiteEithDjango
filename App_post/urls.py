from django.urls import path
from .import views
app_name = 'App_post'
urlpatterns = [
       path('',views.Homepage,name='homepage'),
       path('like/<pk>/',views.liked,name='liked'),
       path('unlike/<pk>/',views.unliked,name='unliked'),
    ]