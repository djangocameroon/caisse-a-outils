from django.urls import path

from . import views

app_name = "toolbox"

urlpatterns = [
    path("", views.home, name="home"),
    path("outils/", views.tool_list, name="tool_list"),
    path("outils/<slug:slug>/", views.tool_detail, name="tool_detail"),
    path("ressources/", views.resource_list, name="resource_list"),
    path("ressources/<slug:slug>/", views.resource_detail, name="resource_detail"),
]
