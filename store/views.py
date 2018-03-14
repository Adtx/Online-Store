from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
#from forms import UserRegistrationForm

#from django.urls import reverse
# from django.contrib.auth.models import User


def home_view(request):
    return render(request, 'store/home.html')


def register_view(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			# login(request, user)
			return redirect('home')
	else:
		form = UserRegistrationForm()
	return render(request, 'store/register.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			# login(request, user)
			return redirect('home')
	else:
		form = AuthenticationForm()
	return render(request, 'store/login.html', {'form': form})








# if (request.POST):
# 		User.objects.create_user(username=request.POST['name'], password=request.POST['password'], email=request.POST['email'])
# 		return HttpResponseRedirect(reverse('home'))
# 	else:
# 		return render(request, 'store/register.html')
