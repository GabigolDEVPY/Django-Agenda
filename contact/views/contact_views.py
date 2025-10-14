from django.http import HttpRequest, HttpResponse
from typing import Any
from django.shortcuts import render
from ..models import Contact

# Create your views here.
def index(request):
    return render(request,'contact/index.html')
    
class Users:
    def __init__(self):
        self.all_users: list[dict[str, Any]] = list(Contact.objects.values())

    def users_view(self, request: HttpRequest) -> HttpResponse:
        return render(request, "contact/home.html", context={"users": self.all_users})
    


