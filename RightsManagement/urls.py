"""
URL configuration for RightsManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app import views

urlpatterns = [
    path("api/getmenu/",views.getmenu),
    path("api/editmenu/",views.editmenu),
    path("api/register/",views.register),
    path("api/getgroup/",views.getgroup),
    path("api/login/",views.login),
    path("api/logout/",views.logout),
    path("api/getuser/",views.getuser),
    path("api/edituser/",views.edituser),
    path("api/changepwd/",views.changepwd),
    path("api/deleteuser/",views.deleteuser),
    path("api/getrights/",views.getrights),
    path("api/editrights/",views.editrights),
]
