from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolios/", views.dynamic_lookup_view, name="dynamic_lookup_view"),
    path("photographers/", views.photographers, name="photographers")
    ]