from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserLoginForm 
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages


class RegisterView(CreateView):
    form_class = UserRegisterForm 
    template_name = 'v01/register.html' # v01 is app name
    success_url = '/login/' # if form is valid, user will redirect to login page
    
    # def form_valid(self, form): #if you want auto login user after registration, you need use this function
    #     user = form.save() #We will save data from form to User 
    #     login(self.request, user) #login user. 
    #     return redirect('home') #redirect user to home page
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Register'
        return context
    

class CustomLoginView(LoginView):
    form_class = UserLoginForm # Custom login form
    template_name = 'v01/login.html' # v01 is app name
    # success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('home')
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)
    
    # Optionally add extra context or override methods.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
    
    
def user_logout(request): #logout view
    logout(request)
    return redirect('login') #after logging out, redirect to login page

def home(request):
    return render(request, 'v01/home.html')