from django.urls import path
from .views import Pages as pages

app_name = 'authentications'
urlpatterns = [

    path('login', pages.login, name='login'),
    path('register', pages.register, name='register')
]
