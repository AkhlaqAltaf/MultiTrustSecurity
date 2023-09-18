from django.urls import path
from .views import Pages as pages
app_name = 'interfaces'
urlpatterns=[

    path('' ,pages.home , name='home' ),




]