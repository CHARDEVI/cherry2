from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ironman(request):
    return HttpResponse('<h1>IAM IRON MAN,WE LOVE YOU 3000</h1>')