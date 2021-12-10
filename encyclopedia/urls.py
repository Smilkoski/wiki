from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search/", views.search, name="search"),
    path("wiki/add/", views.add, name="add"),
    path("wiki/edit/<str:title>/", views.edit, name="edit"),
    path("wiki/random/", views.random, name="random"),
    path("wiki/<str:title>/", views.detail, name="detail"),
]
