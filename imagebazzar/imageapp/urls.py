from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home/',views.index,name='index'),
    path('category/<int:cid>/',views.categoryy,name='categoryy'),
    path('aboutus/',views.aboutus,name='aboutus'),
]
