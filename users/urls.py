from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from users import views

app_name = 'users'

urlpatterns = [
    #  path('', views.index, name='index'),
    path('login', views.UserLoginView.as_view(), name='login'),
    # path('login', views.login, name='login'),
    path('registration', views.UserRegistrationView.as_view(), name='registration'),
    # path('registration', views.registration, name='registration'),
    path('profile/<int:pk>', login_required(views.UserProfileView.as_view()), name='profile'),
    # path('profile', views.profile, name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('logout', views.logout, name='logout'),
    path('verify/<str:email>/<uuid:code>', views.EmailVerificationView.as_view(), name='email_verification'),
]
