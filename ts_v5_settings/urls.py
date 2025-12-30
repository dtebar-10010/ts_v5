from django.contrib import admin
from django.urls import path, include
from ts_v5_app import views

urlpatterns = [
 path( 'admin/', admin.site.urls ),
 path( '', include( 'ts_v5_app.urls' ) ),
 path('test-email/', views.test_email, name='test_email'),  # <-- Add this line
]
