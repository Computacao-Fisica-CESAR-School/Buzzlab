from django.urls import path
from .views import home, register_request, login_request, logout_request

urlpatterns = [
	path('', home),
	path('register/', register_request),
	path('login/', login_request),
	path('logout/', logout_request),
]