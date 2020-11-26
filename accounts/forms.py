from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ShippingInfoForm(forms.Form):
    name = forms.CharField(label="Name", max_length=40)
    city = forms.CharField(label="City", max_length=40)
    state = forms.CharField(label="State", max_length=40)
    zip_code = forms.CharField(label="Zip Code", max_length=5)
    address = forms.CharField(label="Address", max_length=40)


class PaymentInfoForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=40)
    phone = forms.CharField(label="Phone Number", max_length=40)
    name_on_card = forms.CharField(label="Name On Card", max_length=40)
    card_number = forms.CharField(label="Card Number", max_length=40)
    exp = forms.CharField(label="Expiration", max_length=40)
    cvc = forms.CharField(label="CVC", max_length=3)
