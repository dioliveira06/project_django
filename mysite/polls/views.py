# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("Olá Mundo. Essa é uma edição do polls para index.")

# Create your views here.
