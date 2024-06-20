from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login as auth_login, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser
from django.contrib.auth.hashers import check_password
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        role = request.POST['role']
        user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, middle_name=middle_name, role=role)
        login(request, user)
        return redirect('home')
    return render(request, 'authentication/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(f"Attempting login for email: {email}")
        try:
            user = CustomUser.objects.get(email=email)
            print(f"Found user: {user}")
        except CustomUser.DoesNotExist:
            user = None
            print(f"No user found with email: {email}")
        if user is not None and check_password(password, user.password):
            print(f"Password check passed for user: {user.email}")
            user.is_active = True
            user.save()
            auth_login(request, user)
            print(f"User {user.email} logged in successfully!")
            return redirect('home')
        else:
            print("Invalid email or password")
            return render(request, 'authentication/login.html', {'error': 'Invalid email or password'})
    return render(request, 'authentication/login.html')

@login_required
def logout_view(request):
    if request.method == 'POST':
        request.user.is_active = False
        request.user.save()
        logout(request)
        return redirect('home')

def home(request):
    print(f"Authenticated user: {request.user}")
    print(f"Is user authenticated: {request.user.is_authenticated}")
    return render(request, 'authentication/home.html')

def is_librarian(user):
    return user.is_authenticated and user.role == 1

@login_required
@user_passes_test(is_librarian)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'authentication/user_list.html', {'users': users})

@login_required
@user_passes_test(is_librarian)
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    return render(request, 'authentication/user_detail.html', {'user': user})