# from curses import flash
from urllib import request
from django.http import JsonResponse, response, HttpRequest, HttpResponse
from typing import Any
from django.shortcuts import render
from ..models import Contact

# Create your views here.
def index(request):
    return render(
        request,
        'contact/index.html',
    )
    
class Users:
    def __init__(self):
        #return users at function
        self.all_users: list[dict[str, Any]] = list(Contact.objects.values())

    def return_all_users(self, request: HttpRequest) -> HttpResponse:
        print(self.all_users)
        
        return JsonResponse(self.all_users, safe=False)

def users_view(request: HttpRequest) -> HttpResponse:
    print("Chegou aqui")
    return render(
        request,
        'contact/home.html',
    )
    return Users().return_all_users(request)


