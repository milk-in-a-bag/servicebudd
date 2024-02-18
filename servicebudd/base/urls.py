from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('search/<str:cat>/', views.search, name='search'),
    path('search/<str:cat>/<str:name>', views.result, name='result'),
]