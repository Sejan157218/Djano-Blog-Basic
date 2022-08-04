from django.urls import path,include
from . import views

app_name='accounts'
urlpatterns = [
    path('signup/', views.signupPage,name='signup'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logout_view,name='logout'),
]