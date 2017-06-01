from django.shortcuts import render, redirect
from IPython import embed
from .models import User, Message, Comment

# Create your views here.
def index(request):
  return render(request, 'kris_app/index.html')