
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
        path("", TemplateView.as_view(template_name="shop/home.html"), name = "home"),
        path("explore/", TemplateView.as_view(template_name="shop/explore.html"), name = "explore"),  
        
]