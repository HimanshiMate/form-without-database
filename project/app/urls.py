from django.contrib import admin
from django.urls import path
from  .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('regi/',regi,name="regi"),
    path('login/',login,name="login"),
    # path('set/',set,name="set")
]