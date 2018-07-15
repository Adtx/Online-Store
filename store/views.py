from .forms import CostumerRegistrationForm, SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Costumer, Product
import pickle
from django.db.models import Q


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

def product_search_view(request):
	search_term_1 = request.GET.get('q1')
	search_term_2 = request.GET.get('q2', 'as9df8DSA')
	search_results = Product.objects.all().filter(Q(name__icontains=search_term_1) | Q(name__icontains=search_term_2))
	request.session['q1'] = search_term_1
	request.session['q2'] = search_term_2
	return render(request, 'store/search_results.html', {'products': search_results, 'selected1': 'true', 'selected2': 'false'})

def sort_results_view(request):
	search_term_1 = request.session['q1']
	search_term_2 = request.session['q2']
	sort_property = request.POST['sortby']
	if not search_term_2: search_term_2 = 'as9df8DSA'
	search_results = Product.objects.all().filter(Q(name__icontains=search_term_1) | Q(name__icontains=search_term_2)).order_by(sort_property)
	selected_option = request.POST['selected_option']
	selection_info = ['true','false']
	selected1 = selection_info[(0+int(selected_option))%2]
	selected2 = selection_info[(1+int(selected_option))%2]
	return render(request, 'store/search_results.html', {'products': search_results, 'selected1': selected1, 'selected2': selected2})

# def filter_results_view(request):
# 	search_term_1 = request.session['q1']
# 	search_term_2 = request.session['q2']
# 	min = request.POST['min']
# 	max = request.POST['max']
# 	brand = request.POST['brand']
# 	if not search_term_2: search_term_2 = 'as9df8DSA'
# 	if not brand:
# 		search_results = Product.objects.all().filter(Q(name__icontains=search_term_1) | Q(name__icontains=search_term_2)).filter(price between min max)
# 	elif not min:
# 		search_results = Product.objects.all().filter(Q(name__icontains=search_term_1) | Q(name__icontains=search_term_2) & Q(name__icontains=brand)
# 	else:
# 		search_results = Product.objects.all().filter(Q(name__icontains=search_term_1) | Q(name__icontains=search_term_2) & Q(name__icontains=brand).filter(price between min max)
# 	return render(request, 'store/search_results.html', {'products': search_results})
		