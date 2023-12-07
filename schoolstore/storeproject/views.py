from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from storeproject.forms import CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request, 'home.html')





def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)

            # Get the department parameter from the request
            selected_department = request.POST.get('department', '')

            # Redirect to new_page with the selected department parameter
            return HttpResponseRedirect(f'/new={selected_department}')
        else:
            # Handle authentication failure
            pass
    return render(request, 'login.html')


@login_required
def new(request):
    return render(request,'new.html')
@login_required
def submit(request):
    username = request.user.username
    return render(request,'submit.html',{'username': username})


@login_required
def sub(request):
    return render(request,'sub.html')


