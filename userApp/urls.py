from django.urls import path
from .import views
app_name = 'userApp'
urlpatterns = [
    path('sing_up/',views.Sing_up,name='sing_up'),
    path('login/',views.login_page,name='login'),
    path('Logout/',views.Log_out,name='Logout'),
    path('ProfileEdit/',views.P_Edit_page,name='ProfileEdit'),
    path('profile/',views.view_profile,name='profile'),
    path('s_single_user/<username>/',views.Single_user,name='search_Single_user'),
    path('followed/<username>/',views.follow,name='followed'),
    path('unfollow/<username>/',views.unfollow,name='unfollow'),
]