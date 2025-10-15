from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from typing import Any
from django.shortcuts import render, get_object_or_404
from ..models import Contact

# Create your views here.
def index(request):
    return render(request,'contact/index.html')
    
class Users:
    def __init__(self, param=None):
        self.all_users: list[Contact] = list(Contact.objects.all().order_by('-id'))
        if param:
            self.user: Contact = get_object_or_404(Contact, pk=param)

    def users_view(self, request: HttpRequest) -> HttpResponse:
        return render(request, "contact/home.html", context={"users": self.all_users})
    
    def user_view(self, request: HttpRequest) -> HttpResponse:
        return render(request, "contact/contact.html", context={"contact": self.user})
    


def users_json(request: HttpRequest) -> HttpResponse:
    return Users().users_view(request)

def user_detail(request: HttpRequest, id: int) -> HttpResponse:
    return Users(id).user_view(request)