# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from captcha_app.views import register, login_view,dashboard_view, logout_view,captcha_verification_view,process_payment
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('captcha_app.urls')),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('process_payment/', process_payment, name='process_payment'),
    path('captcha-verification/',captcha_verification_view, name='captcha_verification_view'),
    path('logout/', logout_view, name='logout'),
    path('logout-success/', TemplateView.as_view(template_name='logout.html'), name='logout-success'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('captcha_app-verify/', captcha_verification_view, name='captcha_verification'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)