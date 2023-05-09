from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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