from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('cadastrar/', views.cadastrar, name = 'cadastrar'),
    path('perfil/', views.perfil, name = 'perfil'),
    path('login/', auth_views.LoginView.as_view(template_name = 'usuarios/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'usuarios/logged_out.html'), name = 'logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'usuarios/password_change_form.html', success_url=reverse_lazy('usuarios:password_change_done')), name = 'password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'usuarios/password_change_done.html'), name = 'password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'usuarios/password_reset_form.html', email_template_name='usuarios/password_reset_email.html', success_url=reverse_lazy('usuarios:password_reset_done')), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'usuarios/password_reset_done.html'), name = 'password_reset_done'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'usuarios/password_reset_complete.html'), name = 'password_reset_complete'),
    path('password_reset/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'usuarios/password_reset_confirm.html', success_url=reverse_lazy('usuarios:password_reset_complete')), name = 'password_reset_confirm'),
]