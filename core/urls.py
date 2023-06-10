from django.contrib.staticfiles.views import serve
from django.urls import path, re_path
from .views import *

app_name = 'core'

urlpatterns = [
    path('eng', home_eng, name='home2'),
    path('rus', home_rus, name='home1'),
]