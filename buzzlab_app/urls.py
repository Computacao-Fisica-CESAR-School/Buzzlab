from django.urls import path
from .views import home, register_request, login_request, logout_request, my_labs, create_lab

urlpatterns = [
	path('', home),
	path('register/', register_request),
	path('login/', login_request),
	path('logout/', logout_request),
	path("labs/", my_labs),
	path('labs/create/', create_lab)
]