from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("admin/",admin.site.urls),
    path('',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path("home/",views.home_view,name="home"),
    path("userdetail/<int:id>",views.userdetail,name="userdetail")
]
