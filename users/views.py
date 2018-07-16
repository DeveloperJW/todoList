from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
# def login_view(request):
#     login(request)
#     return render(request, 'login.html', {})


def logout_view(request):
    """Log the user out"""
    logout(request)
    return redirect('home')


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username= new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'register.html', context)



