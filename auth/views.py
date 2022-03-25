from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})