from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('a1.URLS')),
    path('admin/', admin.site.urls),

    
]