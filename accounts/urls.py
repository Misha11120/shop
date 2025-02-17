from django.urls import path
from .views import SignInPage, sign_out_page


urlpatterns = [
    path("sign-in/",SignInPage.as_view(), name = "sign-in"), 
    path("sign_out/", sign_out_page, name = "sign-out"),
]