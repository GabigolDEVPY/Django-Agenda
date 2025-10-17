from django.db.models import QuerySet, Q
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
import contact
from ..models import Contact

# Create your views here.
def create(request):
    return render(request,'contact/create.html')
    