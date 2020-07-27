from django.urls import path
from django.contrib.auth import views as AuthViews
from .views import ProfileView, SignupView, ActivateAccountView, CustomLoginView

urlpatterns = [
    path('', ProfileView, name="profile"),
    path('login/', CustomLoginView, name="login"),
    path('signup/', SignupView, name="signup"),
    path('activate/<uidb64>/<token>/', ActivateAccountView, name='activate'),
    path('logout/', AuthViews.LogoutView.as_view(), name="logout"),
]