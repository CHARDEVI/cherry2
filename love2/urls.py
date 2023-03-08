from love2.views import *
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('ironman/',ironman,name='ironman'),
]