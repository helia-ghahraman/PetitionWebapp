from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView, View)
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.urls import reverse
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import User
from .filters import UserFilter


class UserSignUpView(CreateView):
    form_class = SignUpForm
    model = User

    def get_success_url(self):
        return reverse('user_app:user-list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PrivateProfileForm
    model = User

    def has_permission(self, pk):
        return pk == self.request.user.pk

    def get_success_url(self):
        return reverse('user_app:user-detail', kwargs={'pk': self.request.user.id})
    

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    

class UserListView(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 10

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        filterset = UserFilter(
            self.request.GET, queryset=self.get_queryset().order_by('id'))
        context['filterset'] = filterset
        return context 


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'user_app/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, context={'form': form})
        
    def post(self, request):
        """
        Login user.
        User will be redirected to change password view on their first login.
        """
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_app:user-homepage')
        else:
            return render(request, self.template_name, context={'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user_app:user-login')


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'user_app/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
        

class ChangePasswordView(View):
    form_class = SetPasswordForm
    template_name = 'user_app/change_password.html'

    def get(self, request, pk):
        form = self.form_class(None)
        return render(request, self.template_name, context={'form': form})
        
    def post(self, request, pk):
        form = self.form_class(user=User.objects.get(pk=pk), data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_app:user-login')
        else:
            return render(request, self.template_name, context={'form': form})
