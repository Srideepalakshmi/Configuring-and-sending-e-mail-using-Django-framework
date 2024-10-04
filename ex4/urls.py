from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ex4app.urls')),  # Link to app URLs (correct the app name to `ex4app`)
]
