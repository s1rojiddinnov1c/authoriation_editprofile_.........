from django.urls import path
from .views import (SignUpApiView, 
                    LoginApiView, 
                    UpdateTokenApiView, 
                    LogoutApiView, 
                    ChangePasswordView, 
                    UserProfileView,
                    PasswordResetView,
                    PasswordResetViaCodeView,
                
                    )

urlpatterns = [
    path('signup/', SignUpApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('update_token/', UpdateTokenApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),
    path('password_change/', ChangePasswordView.as_view()),
    path('personal_data/', UserProfileView.as_view()),
    path('reset_password/',PasswordResetView.as_view()),
    path('resetvia_password/',PasswordResetViaCodeView.as_view())
]