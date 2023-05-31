from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Lab, Address, OpeningHours
from django.forms import TimeInput, formset_factory
from crispy_forms.helper import FormHelper

# Django comes with a pre-built register form called UserCreationForm that connects to the pre-built model User.
# However, the UserCreationForm only requires a username and password. To customize the pre-built form, call
# UserCreationForm within a new class called NewUserForm and add the desired custom fields and save the user.
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class CreateLabForm(forms.ModelForm):
    class Meta:
        model = Lab
        exclude = ['address', 'opening_hours', 'admins']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class OpeningHoursForm(forms.ModelForm):
    class Meta:
        model = OpeningHours
        exclude = ['weekday']
        widgets = {
            "open_time": TimeInput(attrs={'type': 'time'}),
            "close_time": TimeInput(attrs={'type': 'time'}),
        }

OpeningHoursFormset = formset_factory(OpeningHoursForm, extra=7)