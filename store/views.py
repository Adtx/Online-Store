from .forms import CostumerRegistrationForm, SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Costumer, Product


def home_view(request):
	on_sale = Product.objects.all().filter(is_on_sale=True)
	new = Product.objects.all().filter(is_new=True)
	best_sellers = Product.objects.all().filter(is_bestseller=True)
	return render(request, 'store/home.html', {'products_on_sale': on_sale, 'new_products': new, 'best_sellers': best_sellers})


def register_view(request):
	if request.method == 'POST':
		form = CostumerRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
	else:
		form = CostumerRegistrationForm()
	return render(request, 'store/register.html', {'form': form})

def update_profile_view(request):
	if request.method == 'POST':
		request.user.username = request.POST['name']
		request.user.email = request.POST['email']
		Costumer.objects.filter(id=request.user.id).update(password=request.POST['newpassword'])
		request.user.telephone = request.POST['telephone']
		request.user.street = request.POST['street']
		request.user.city = request.POST['city']
		request.user.district = request.POST['district']
		request.user.zipcode = request.POST['zipcode']
		request.user.country = request.POST['country']
		request.user.save()
		return redirect('profile')
	if request.user.is_authenticated:
		return render(request, 'store/update_profile.html', {'user': request.user})
	return redirect('home')
		

def profile_view(request):
	if request.user.is_authenticated:
		return render(request, 'store/profile.html')
	return redirect('home')


def login_view(request):
	if request.method == 'POST':
		form = SignInForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('home')
	else:
		form = SignInForm()
	return render(request, 'store/login.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('home')

def product_details_view(request, ean):
	product = Product.objects.get(ean=ean)
	return render(request, 'store/product_details.html', {'product': product})