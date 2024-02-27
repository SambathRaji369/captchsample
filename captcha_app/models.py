from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('recharge', 'Recharge'), ('withdraw', 'Withdraw')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    order_id = models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_gateway = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, default='Pending')


