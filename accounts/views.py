from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context = {'page_title': 'Welcome Home'}
    return render(request, 'accounts/index.html', context)

def register(request):
    registration_form = RegistrationForm(request.POST or None)
    
    if request.method == 'POST' and registration_form.is_valid():
        registration_form.save()
        return redirect('accounts:user_login')
        
    
    context = {
        'page_title': 'Register Now!',
        'registration_form': registration_form,
    }
    return render(request, 'accounts/register.html', context)

def user_login(request):
    login_form = LoginForm()
    context = {
        'page_title': 'Login Now!',
        'login_form': login_form
    }
    
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('accounts:index')
        else:
            return render(request, 'accounts/user_login.html', context)
        
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('accounts:index')
            else:
                return redirect('accounts:user_login')
            

def user_logout(request):
    context = {'page_title': 'Logout !'}
    
    if not request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        if request.POST['logout'] == 'YES':
            logout(request)
            return redirect('index')
    
    return render(request, 'accounts/user_logout.html', context)