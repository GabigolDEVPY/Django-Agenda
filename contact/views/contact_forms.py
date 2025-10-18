from django.db.models import QuerySet, Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from contact.forms import ContactForm
from contact.models import Contact


# Create your views here.
def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact:index")
        context = {'form': form, "title": "Criar Contato"}
        return render(request,'contact/create.html', context)
    
    context = {'form': ContactForm()}
    return render(request,'contact/create.html', context)
    
def update(request, id):
    contact = get_object_or_404(Contact, id=id)
    
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact:users")  
        context = {'form': form, 'contact': contact, "title": "Atualizar Contato"}
        return render(request, 'contact/update.html', context)
    
    form = ContactForm(instance=contact)
    context = {'form': form, 'contact': contact, "title": "Atualizar Contato"}
    return render(request, 'contact/create.html', context)   