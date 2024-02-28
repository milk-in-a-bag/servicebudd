from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import ServiceProvider
from .forms import ServiceProvidersNameFilterForm
from .filters import ServiceProviderFilter

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

def result(request, cat, name):
    name = request.GET.get('name')
    spots = ServiceProvider.objects.all()

    if name:
        spots = spots.filter(name__icontains=name)

    context = {
        'spots': spots,
        'category': cat,
    }

    return render(request, 'result.html', context)