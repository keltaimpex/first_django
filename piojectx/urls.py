from django.contrib import admin
from django.urls import path, include
from portfolio import views  # Replace `myapp` with your app's name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Root URL
    path('contact/', include('portfolio.urls')),  # App URLs for contact
]
