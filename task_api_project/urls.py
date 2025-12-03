from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This connects the 'api/' path to your app's urls
    path('api/', include('tasks.urls')), 
    
    # Optional: Adds the 'Log in' button to the API browser
    path('api-auth/', include('rest_framework.urls')), 
]
