from django.urls import path

from userauths import views
app_name = 'userauths'

urlpatterns = [
  path("signup/", views.RegisterView,name="signup"),
  path('user_login/',views.user_login , name= 'user_login'),
  path('logout_user/',views.logout_user , name= 'logout_user'),

]