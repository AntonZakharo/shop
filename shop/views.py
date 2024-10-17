from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomUserCreationForm
from .models import Item


@login_required
def product_list(request):
    products = Item.objects.all()
    return render(request, 'products_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Item, id=product_id)
    return render(request, 'product_page.html', {'product': product})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def cart(request):
    return HttpResponse("<h1>Эта страница ещё не готова, она появится позже.</h1>")


def profile(request):
    return HttpResponse("<h1>Эта страница ещё не готова, она появится позже.</h1>")


def home(request):
    return HttpResponse("home")


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})
