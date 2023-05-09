from django.urls import path
from .views import home, register_request

urlpatterns = [
    path('', home),
	path('register/', register_request)
]