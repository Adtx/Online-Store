from .forms import CostumerRegistrationForm, SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Costumer, Product
from django.db.models import Q
from functools import reduce
from .cart import *
import operator


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
	return render(request, 'store/product_details.html', {'product': product, 'ean': product.ean})

def product_search_view(request):
	search_term_1 = request.session['q1'] = request.GET.get('q1')
	search_term_2 = request.session['q2'] = request.GET.get('q2', 'as9df8DSA')
	search_results = Product.objects.all().filter(Q(name__icontains=search_term_1) | Q(name__icontains=search_term_2) | Q(brand__iexact=search_term_1) | Q(category__iexact=search_term_1) | Q(category__iexact=search_term_2) | Q(description__icontains=search_term_1) | Q(description__icontains=search_term_2))
	if 'brands' in request.session: del request.session['brands']
	if 'min' in request.session or 'max' in request.session: 
		del request.session['min']
		del request.session['max']
	request.session.modified = True
	brands = ['Intel','Apple','Asus','BenQ','Samsung','HP','LG','Lenovo','MSI','Philips']
	checkboxclass = {}
	for brand in brands:
		checkboxclass[brand] = 'm-checkbox-unchecked'
	return render(request, 'store/search_results.html', {'products': search_results, 'selected1': 'true', 'selected2': 'false', 'min': 0, 'max': 4300, 'checkboxclass': checkboxclass})

def sort_results_view(request):
	search_term_1 = request.session['q1']
	search_term_2 = request.session['q2']
	sort_property = request.POST['sortby']
	if not search_term_2: search_term_2 = 'as9df8DSA'
	
	selected_option = request.POST['selected_option']
	selection_info = ['true','false']
	selected1 = selection_info[(0+int(selected_option))%2]
	selected2 = selection_info[(1+int(selected_option))%2]

	search_terms = [Q(name__icontains=search_term_1), Q(name__icontains=search_term_2)]

	if 'brands' in request.session:
		brand_filters = []
		for brandName in request.session['brands']:
			brand_filters.append(Q(name__icontains=brandName))
		search_results = Product.objects.all().filter(reduce(operator.or_, search_terms)).filter(reduce(operator.or_, brand_filters)).order_by(sort_property)
	else:
		search_results = Product.objects.all().filter(reduce(operator.or_, search_terms)).order_by(sort_property)

	return render(request, 'store/search_results.html', {'products': search_results, 'selected1': selected1, 'selected2': selected2})


def filter_results_view(request):
	search_term_1 = request.session['q1']
	search_term_2 = request.session['q2']
	
	if not search_term_2: search_term_2 = 'as9df8DSA'
	if 'min' in request.session or 'max' in request.session:
		min = request.session['min']
		max = request.session['max']
	else:
		min = 0
		max = 4300
	brand_filters = []

	brand = request.GET.get('brand')
	if brand != None:
		if 'brands' not in request.session:
			request.session['brands'] = [brand]
		elif brand in request.session['brands']:
			request.session['brands'].remove(brand)
		else:
			request.session['brands'].append(brand)
	else:
		priceRangeString = request.POST['priceRange']
		priceRangeString = priceRangeString.replace("&nbsp;", " ")

		minMaxList = [int(s) for s in priceRangeString.split() if s.isdigit()]

		if len(minMaxList) == 2:
			min = minMaxList[0]
			max = minMaxList[1]
		elif len(minMaxList) == 3:
			min = minMaxList[0]
			max = minMaxList[1] * 1000 + minMaxList[2]
		else:
			min = minMaxList[0] * 1000 + minMaxList[1]
			max = minMaxList[2] * 1000 + minMaxList[3]

		request.session['min'] = min
		request.session['max'] = max

	request.session.modified = True
	
	if 'brands' in request.session:
		for brandName in request.session['brands']:
			brand_filters.append(Q(name__icontains=brandName))

	search_terms = [Q(name__icontains=search_term_1), Q(name__icontains=search_term_2)]

	if len(brand_filters) > 0:
		search_results = Product.objects.all().filter(reduce(operator.or_, search_terms)).filter(reduce(operator.or_, brand_filters)).filter(price__gte=min,price__lte=max)
	else:
	 	search_results = Product.objects.all().filter(reduce(operator.or_, search_terms)).filter(price__gte=min,price__lte=max)

	brands = ['Intel','Apple','Asus','BenQ','Samsung','HP','LG','Lenovo','MSI','Philips']
	checkboxclass = {}
	for brand in brands:
		if brand in request.session['brands']:
			checkboxclass[brand] = "m-checkbox-checked"
		else:
			checkboxclass[brand] = "m-checkbox-unchecked"
	return render(request, 'store/search_results.html', {'products': search_results, 'min': min, 'max': max, 'checkboxclass': checkboxclass})

def show_cart_view(request):
	items = get_cart_items(request)
	cart_total = cart_subtotal(request)
	return render(request, 'store/shopping_cart.html', {'cart_items': items, 'cart_total': cart_total})

def add_cart_item_view(request):
	#add to cart
	add_to_cart(request)
	return redirect(request.META['HTTP_REFERER'])

def remove_cart_item_view(request):
	remove_from_cart(request)
	return redirect('show_cart')

def update_cart_item_view(request):
	update_cart(request)
	return redirect('show_cart')
