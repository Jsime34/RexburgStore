from django.shortcuts import render
from django.http import HttpResponse


def loginpage(response):
    return render(response, "loginpage/loginpage.html", {})

