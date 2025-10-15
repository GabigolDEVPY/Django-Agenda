from os import name
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from typing import Any
from django.shortcuts import render, get_object_or_404

import contact
from contact.admin import ContactAdmin
from ..models import Contact

# Create your views here.
def index(request):
    return render(request,'contact/index.html')
    
class Users:
    def __init__(self, param=None):
        self.all_users: list[dict[str, Any]] = list(Contact.objects.all().order_by('-id'))
        if param:
            self.user: Contact = get_object_or_404(Contact.objects.filter(pk=param))

    def users_view(self, request: HttpRequest) -> HttpResponse:
        return render(request, "contact/home.html", context={"users": self.all_users})
    
    def user_view(self, request: HttpRequest) -> HttpResponse:
        return render(request, "contact/contact.html", context={"contact": self.user})
    


