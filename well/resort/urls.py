from django.urls import path

from resort import views

urlpatterns = [
  path("resort/", views.signup,name="resort")
]