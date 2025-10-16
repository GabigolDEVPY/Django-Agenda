from django.db.models import QuerySet, Q
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
import contact
from ..models import Contact

# Create your views here.
def index(request):
    return render(request,'contact/index.html')
    
class Users:
    def __init__(self, param=None, search=None):
        self.all_users: Contact = Contact.objects.all().order_by('-id')
        if param:
            self.user: Contact = get_object_or_404(Contact, pk=param)
        elif search:
            self.result_search: contact = \
            Contact.objects.filter(Q(first_name__icontains=search) | 
            Q(last_name__icontains=search) | 
            Q(email__icontains=search) |     
            Q(description__icontains=search))    

    def users_view(self, request: HttpRequest) -> HttpResponse:
        contacts = self.all_users
        paginator = Paginator(contacts, 10)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)
        context = {
            "page_object": page_object,
        }
        return render(request, "contact/home.html", context=context)
    
    def user_view(self, request: HttpRequest) -> HttpResponse:
        return render(request, "contact/contact.html", context={"contact": self.user})
    
    def user_search(self, request: HttpRequest) -> HttpResponse:
        contacts = self.result_search
        paginator = Paginator(contacts, 10)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)
        context = {
            "page_object": page_object,
        }
        return render(request, "contact/home.html", context=context)


def users_json(request: HttpRequest) -> HttpResponse:
    return Users().users_view(request)

def user_detail(request: HttpRequest, id: int) -> HttpResponse:
    return Users(id).user_view(request)

def search(request: HttpRequest) -> HttpResponse:
    value_search = request.GET.get("q").strip()
    if value_search == '':
        return redirect('contact:users')
    print(value_search)
    return Users(search=value_search).user_search(request)