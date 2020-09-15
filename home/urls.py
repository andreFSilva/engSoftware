from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


