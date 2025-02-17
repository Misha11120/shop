from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

def sign_out_page(request):
    logout(request)
    return redirect("sign-in")
class SignInPage(View):
    def get(self, request):
        return render(request, "accounts/sign-in.html")
    def post(self, request):
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        user = authenticate(request, username = user_name, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        return render(request, "accounts/sign-in.html", context={
            "error": "username or password is incorrect"
        })
