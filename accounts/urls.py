from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm,PwdResetForm,PwdResetConfirmForm
from . import views
from django.views.generic import TemplateView


app_name='accounts'
urlpatterns=[
     path('login/', auth_views.LoginView.as_view(template_name='accounts/registration/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page= '/accounts/login/'), name='logout'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/user/password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='accounts/user/password_reset_email.html',
                                                                 form_class=PwdResetForm), name='pwdreset'),
     path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/user/password_reset_confirm.html',
                                                                                                success_url='/accounts/password_reset_complete/', 
                                                                                                form_class=PwdResetConfirmForm),
         name="password_reset_confirm"),
         path('password_reset/password_reset_email_confirm/',
         TemplateView.as_view(template_name="accounts/user/reset_status.html"), name='password_reset_done'),
    path('password_reset_complete/',
         TemplateView.as_view(template_name="accounts/user/reset_status.html"), name='password_reset_complete'),

    path('activate/<slug:uidb64>/<slug:token>/',views.activate,name='activate'),
    path('profile/edit/', views.edit_details, name='edit_details'),
    path('profile/delete_user/', views.delete_user, name='delete_user'),
    path('profile/delete_confirm/', TemplateView.as_view(template_name="accounts/user/delete_confirm.html"), name='delete_confirmation'),
    path('addresses/',views.view_address,name='addresses'),
    path('add_address',views.add_address,name='add'),
    path('edit_address/<slug:id>/',views.edit_address,name='edit'),
    path('delete_address/<slug:id>/',views.delete_address,name='delete'),
    path('set_default/<slug:id>/',views.set_default,name='default'),
    path('user_order',views.user_orders,name='user_orders'),
]