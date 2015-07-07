from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

def index(req):
    return(render(req,'base.html'))
# Create your views here.
