# from curses import flash
from urllib import request
from django.http import JsonResponse, response, HttpRequest, HttpResponse
from typing import Any
from django.shortcuts import render
from ..models import Contact

# Create your views here.
def index(request):
    return render(request,'contact/index.html')
    
class Users:
    def __init__(self):
        self.all_users: list[dict[str, Any]] = list(Contact.objects.values())

def users_view(request: HttpRequest) -> HttpResponse:
    return render(request, "contact/home.html", context={"users": Users().all_users})


