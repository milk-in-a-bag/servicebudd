from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('categories/<str:cat>/', views.categories, name='categories'),
    path('result', views.result, name='result'),
    path('search/<str:name>', views.search, name='search'),
]