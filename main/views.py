from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1> Hello World </h1>")

def login(response):
    return HttpResponse("There is a login page for you bro")
