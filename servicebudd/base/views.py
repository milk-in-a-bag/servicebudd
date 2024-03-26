from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import ServiceProvider, Filter, Review
from .forms import ServiceProvidersNameFilterForm
from .filters import ServiceProviderFilter
from rest_framework import generics
from .serializers import FilterSerializer
import requests
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'There exists an account for this email')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'There exists an account with this name')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')

    else:
        return render(request, 'login.html')
    
def categories(request, cat):

    service_filter = ServiceProviderFilter(request.GET, queryset=ServiceProvider.objects.all())

    service = ServiceProvider.objects.filter(category__iexact=cat)

    context = {
        'category': cat, 
        'form': ServiceProvidersNameFilterForm(),
        'service': service,
        'service2': service_filter.qs,
        'form2': service_filter.form
    }

    return render(request, 'categories.html', context)

def search(request, name):
    name = request.GET.get('name')

    spots = ServiceProvider.objects.all()
    service_filter = ServiceProviderFilter(request.GET, queryset=ServiceProvider.objects.all())

    if name:
        spots = spots.filter(name__icontains=name)
        service_filter = ServiceProviderFilter(request.GET, queryset=ServiceProvider.objects.none())
    else:
        spots = ServiceProvider.objects.none()

    context = {
        'name': name,
        'spots': spots,
        'service2': service_filter.qs,
    }
    
    return render(request, 'search.html', context)

class FilterList(generics.ListCreateAPIView):
    serializer_class = FilterSerializer

    def get_queryset(self):
        queryset = Filter.objects.all()

        return queryset


class FilterDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FilterSerializer
    queryset = Filter.objects.all()

def result(request):
    response = requests.get('http://127.0.0.1:8000/filter/47').json()

    location = response.get('location')
    starting_price = response.get('starting_price')
    category = response.get('category')


    queryset = ServiceProvider.objects.all()

            # Add filters conditionally based on the provided parameters
    if location:
        queryset = queryset.filter(location=location)
    if starting_price:
        queryset = queryset.filter(starting_price=starting_price)
    if category:
        queryset = queryset.filter(category=category)

    return render(request, 'result.html', {'queryset': queryset})

@login_required
def spots(request, name):
    reviews = Review.objects.all()

    if request.method == 'POST':
        user = request.user
        service_provider_name = name  # Assuming name is the service provider's name

        # Retrieve the ServiceProvider instance corresponding to the name
        service_provider = get_object_or_404(ServiceProvider, name=service_provider_name)

        rating = request.POST['rating']
        rating = request.POST['rating']
        comment = request.POST['comment']
        
        review = Review.objects.create(user=user, service_provider=service_provider, rating=rating, comment=comment)
        review.save()

        return redirect('spots', name=name)

    context = {'name': name, 'reviews': reviews}
    return render(request, 'spots.html', context)