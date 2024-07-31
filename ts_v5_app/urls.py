# from django.core.mail import send_mail
from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from . import views

urlpatterns = [
 path( '', views.home, name = 'home' ),
 path( 'favicon.png', RedirectView.as_view( url = staticfiles_storage.url( 'img/icons/favicon.png' ) ) ),
 path( 'contact/', views.contact, name = 'contact' ),
 path( 'download_resume/', views.download_resume, name = 'resume' ),
]
