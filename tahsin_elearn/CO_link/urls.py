from django.contrib import admin
from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static
from . import views as COF

urlpatterns = [
   
    path('admin/', v.index,name='courseadmin'),
    path('checkout/', COF.CO_fun,name='ckout'),
]

