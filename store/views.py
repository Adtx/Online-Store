from .forms import CostumerRegistrationForm, SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


def home_view(request):
    return render(request, 'store/home.html')


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
		request.user.telephone = request.POST['telephone']
		request.user.street = request.POST['street']
		request.user.city = request.POST['city']
		request.user.district = request.POST['district']
		request.user.zipcode = request.POST['zipcode']
		request.user.country = request.POST['country']
		request.user.save()
		return redirect('profile')
	return render(request, 'store/update_profile.html', {'user': request.user})

def profile_view(request):
	return render(request, 'store/profile.html')


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