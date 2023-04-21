from django.urls import path, include

from users import views

app_name = 'users'

urlpatterns = [
    #  path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
]