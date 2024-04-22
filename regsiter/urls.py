from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('details/<int:user_id>/', views.get_user_detail, name='get user details'),
    path('profile/update/<int:user_id>/', views.update_profile, name='update_profile'),
]
