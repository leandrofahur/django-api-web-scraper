from django.urls import path
from .views import CustomTokenObtainPairView, LogoutView , UserView

urlpatterns = [
    path('', UserView.as_view(), name='users'),
    path('<int:user_id>', UserView.as_view(), name='user'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
]