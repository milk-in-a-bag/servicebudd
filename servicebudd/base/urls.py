from django.urls import path
from . import views
from .views import FilterList, FilterDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('categories/<str:cat>/', views.categories, name='categories'),
    path('result', views.result, name='result'),
    path('search/<str:name>', views.search, name='search'),
    path('filter/', FilterList.as_view()),
    path('filter/<int:pk>', FilterDetail.as_view()),
    path('spots/<str:name>', views.spots, name='spots'),
]