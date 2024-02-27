from django import forms
from captcha.fields import CaptchaField

class CaptchaForm(forms.Form):
    captcha = CaptchaField()

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class PaymentForm(forms.Form):
    order_id = forms.CharField()
    amount = forms.CharField()
    payment_gateway = forms.ChoiceField(choices=[('googlepay', 'Google Pay'), ('paytm', 'Paytm'), ('phonepe', 'PhonePe')])
  