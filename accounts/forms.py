from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


# the UserCreationForm only gives Password and confirm password
# and we do not need to include them to the fields cause they comes automatically to the template
# and getting the remaining needed fields from the default User model
class CreateUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username','email']
		label = {'email':'Email'}