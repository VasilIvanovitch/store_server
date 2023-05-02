# from django.contrib import auth, messages
# from django.contrib.auth.decorators import login_required
# from pyexpat import model

from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Регистрация завершена успешно'
    title = 'Store - Регистрация'
    # def get_context_data(self, **kwargs):
    #     context = super(UserRegistrationView, self).get_context_data()
    #     context['title'] = 'Store - Регистрация'
    #     return context


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileView, self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user=self.object)
    #     context['title'] = 'Store - Личный кабинет'
    #     return context
    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object.id])


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        print(code)
        user = User.objects.get(email=kwargs['email'])
        print(user)
        email_verifications = EmailVerification.objects.filter(user=user, code=code)

        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            HttpResponseRedirect(reverse('index'))

# http://localhost:8000/users/verify/ver@ver.com/f13db816-0123-4546-a6d9-7ad31bde5d95
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             # password = form.cleaned_data['password']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         #form1= form.cleaned_data
#         #print(form.cleaned_data)
#         if form.is_valid():
#             print("Registration successful")
#             form.save()
#             messages.success(request, 'Регистрация завершена успешно')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#     context = {'title': 'Store - Профиль',
#                'form': form,
#                 'baskets': Basket.objects.filter(user=request.user),     #filter(id=id)
#                }
#     return render(request, 'users/profile.html', context)

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))
