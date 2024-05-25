from django.urls import path
from .views import RegisterView, CustomLoginView, user_logout, home

urlpatterns = [
path('', home , name='home'),
path('register/', RegisterView.as_view(), name='register'),
path('login/', CustomLoginView.as_view(), name='login'),
path('logout/', user_logout, name='logout'),
]

