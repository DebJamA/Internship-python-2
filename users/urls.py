from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<uuid:pk>', ProfileUserView.as_view(), name='profile'),
    path('update/<uuid:pk>', UpdateProfileUserView.as_view(), name='update_profile'),
]
