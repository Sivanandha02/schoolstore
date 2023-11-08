
from django.urls import path
from .views import contact_page,demo
app_name='myprojectapp'
urlpatterns = [
    path('',demo, name='demo'),
    path('contact', contact_page, name='contact'),


]