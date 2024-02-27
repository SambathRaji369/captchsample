# urls.py
from django.urls import path
from .views import process_payment

urlpatterns = [
    path('process_payment/', process_payment, name='process_payment'),
    # path('success/', success_page, name='success_page'),
    # path('failure/', failure_page, name='failure_page'),
]

