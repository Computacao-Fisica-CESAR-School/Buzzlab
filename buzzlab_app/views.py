from django.shortcuts import render, redirect
from .forms import NewUserForm, CreateLabForm, AddressForm, OpeningHoursFormset
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Lab, UserProfile

def home(request):
    return render(request, "home.html")

def register_request(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")

def my_labs(request):
	if request.user.is_authenticated:
		try:
			curr_user_profile = UserProfile.objects.get(user=request.user)
		except ObjectDoesNotExist:
			labs = Lab.objects.none()
		else:
			labs = Lab.objects.filter(admins=curr_user_profile)
		return render(request, "labs.html", {"labs": labs})
	messages.info(request, "You need to be logged in to access that page.")
	return redirect("/login")

def create_lab(request):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if request.method == 'POST':
        lab_form = CreateLabForm(request.POST)
        address_form = AddressForm(request.POST)
        opening_hours_formset = OpeningHoursFormset(request.POST)
        
        if lab_form.is_valid() and address_form.is_valid() and opening_hours_formset.is_valid():
            lab = lab_form.save(commit=False)
            address = address_form.save()
            lab.address = address
            lab.save()
            for form, wd in zip(opening_hours_formset, weekdays):
                oh_form = form.save(commit=False)
                oh_form.weekday = wd
                oh_form.save()
                lab.opening_hours.add(oh_form)
            lab.admins.add(request.user.userprofile)
            return redirect('/labs')
    else:
        lab_form = CreateLabForm()
        address_form = AddressForm()
        opening_hours_formset = OpeningHoursFormset()

    return render(request, 'create_lab.html', {'lab_form': lab_form, 'address_form': address_form, 'oh_formset': opening_hours_formset, 'oh_formset_weekdays': zip(opening_hours_formset, weekdays)})

def manage_lab(request, id):
    #TODO: block current user if they are not an admin for this lab
    lab = Lab.objects.get(id=id)
    opening_hours = lab.opening_hours.all()
    admins = lab.admins.all()
    return render(request, "manage_lab.html", {'lab': lab, 'opening_hours': opening_hours, 'admins': admins})