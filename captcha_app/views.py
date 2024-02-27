from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm,PaymentForm
from .models import User,Payment
from django.contrib.auth.decorators import login_required
import requests

def process_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            order_id = form.cleaned_data['upi_id']
            amount = form.cleaned_data['amount']
            payment_gateway = form.cleaned_data['payment_gateway']

            if payment_gateway == 'googlepay':
                # Google Pay integration code
                # Replace the placeholders with actual values
                googlepay_url = 'https://googlepayapi.example.com/process_payment'
                response = requests.post(googlepay_url, data={'order_id': order_id, 'amount': amount})
            elif payment_gateway == 'paytm':
                paytm_url = 'https://paytmapi.example.com/process_payment'
                response = requests.post(paytm_url, data={'order_id': order_id, 'amount': amount})

            elif payment_gateway == 'phonepe':
                # PhonePe integration code
                phonepe_url = 'https://api-preprod.phonepe.com/apis/pg-sandbox/pg/v1/pay'
                response = requests.post(phonepe_url, data={'order_id': order_id, 'amount': amount})


            # Process the response from the payment gateway
            if response.status_code == 200:
                # Update payment status in the database
                Payment.objects.create(order_id=order_id, amount=amount, payment_gateway=payment_gateway,
                                       payment_status='Success')

                # Redirect to the dashboard page on successful payment
                return redirect('dashboard')  # Change 'dashboard' to the actual URL name of your dashboard page
            else:
                # Payment failed
                Payment.objects.create(order_id=order_id, amount=amount, payment_gateway=payment_gateway,
                                       payment_status='Failed')
                return redirect('failure_page')

    else:
        form = PaymentForm()

    return render(request, 'payment_form.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})


def captcha_verification_view(request):
    if request.method == 'POST':
        return render(request, 'captcha_verified.html')
    else:
        return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']

            if password == password_confirm:
                # Create a new user
                user = User.objects.create_user(username=phone_number, password=password, email=email, first_name=name)
                login(request, user)

                # Add a success message
                messages.success(request, 'Registration successful. You can now login.')

                return redirect('login')  # Redirect to the login page after successful registration
            else:
                form.add_error('password_confirm', 'Passwords do not match.')

    else: 
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            user = authenticate(request, username=phone_number, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to your dashboard or another page
            else:
                form.add_error('password', 'Invalid login credentials.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
