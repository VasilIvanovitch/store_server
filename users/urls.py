from django.urls import path, include
from django.contrib.auth.views import LogoutView
from users import views

app_name = 'users'

urlpatterns = [
    #  path('', views.index, name='index'),
    path('login', views.UserLoginView.as_view(), name='login'),
    # path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('logout', views.logout, name='logout'),
]