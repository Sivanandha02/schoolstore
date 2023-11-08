from . import views
from django.urls import path
app_name='registrationapp'
urlpatterns = [
    path('register',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact_page, name='contact'),
]
