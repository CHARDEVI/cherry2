from love.views import *
from django.urls import path

app_name='something'

urlpatterns=[
    path('captain/',captain,name='captain'),
]