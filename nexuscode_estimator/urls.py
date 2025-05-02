from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estimator.urls')),  # 👈 This connects your app's URL
]
