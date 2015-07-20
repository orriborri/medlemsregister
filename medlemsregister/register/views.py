from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

def index(req):
    return(render(req,'index.html'))

def add():
    return

def add_member():
    return
# Create your views here.
