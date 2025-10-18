from django.db.models import QuerySet, Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from contact.forms import ContactForm


# Create your views here.
def create(request):
    if request.method == "POST":
        print("request é post")
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact:create")
        context = {'form': form}
        return render(request,'contact/create.html', context)
    
    context = {'form': ContactForm()}
    return render(request,'contact/create.html', context)
    
    