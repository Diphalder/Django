from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# rqst -> responds
# rqsr handler
# action 

def say_hello(request):
    # pull data form db
    # transform
    # send email
    return HttpResponse('hello world')

def renderhtmlfile(request):
    # pull data form db
    # transform
    # send email
    return render(request,'hello.html' , { 'nameVar' : 'Dip Halder'})


