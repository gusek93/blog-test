from django.urls import path
from .views import (
    RegisterUserView,
)

urlpatterns = [
    path(r'auth/register', RegisterUserView.as_view())
]
