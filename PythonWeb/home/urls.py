from django.urls import path
from .  import views
from django.contrib.auth import views as vi
urlpatterns = [
    path('',views.index),
    path('contact/', views.contact,name='contact'), 
    path('register/',views.register,name='register'),
    path('login/',vi.login,{'template_name':'pages/login.html'},name = 'login'),
    path('logout/',vi.logout,{'next_page':'/'},name = 'logout')]