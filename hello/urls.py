from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("companyc",views.companyc,name="companyc"),
    path("main/",views.main,name="main"),
    path("main1/",views.main1,name="main1"),
    path("stat",views.stat,name="stat"),
    path("contact",views.contact,name="contact"),
    path("contactus",views.contactus,name="contactus"),
    path("placed",views.placed,name="placed"),
    path("companies_visited",views.companies_visited,name="companies_visted"),
    path('login/',views.login_view,name="login_view"),
    path('register/',views.register,name="register"),
    path("logout_page",views.logout_page,name="logout_page"),
    path("sprofile",views.sprofile,name="sprofile"),
    path("dsa/",views.dsa,name="dsa"),
    path("java/",views.java,name="java"),
    path("python",views.python,name="python"),
    path("dbms",views.dbms,name="dbms"),
    path("c/",views.c,name="c"),
    path("apt/",views.apt,name="apt"),
    path("sql",views.sql,name="sql"),
    path("front",views.front,name="front"),
    path("back",views.back,name="back"),
    path("english",views.english,name="english")
]

