from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

# Create your views here.
def index(request):
    return render(request, "index.html")


@login_required(login_url='index')
def dashboard(request):
    return render(request, "triangle/dashboard.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists. Please choose a different username."
            return render(request, 'index.html', {'error_message': error_message})

        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('dashboard')  # Replace 'dashboard' with the URL name of your dashboard page

    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'home' with the URL name of your home page
        else:
            # Authentication failed
            error_message = "Invalid username or password"
            return render(request, 'index.html', {'error_message': error_message})

    return render(request, 'index.html')