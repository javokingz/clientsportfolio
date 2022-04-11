from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import ContactForm

from django.core.mail import EmailMessage
# Create your views here.


def Contact(request):
    template = 'contact.html'
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Si todo salio bien redireccionamos
            email = EmailMessage(
                "Contaco de Prueba",
                "De {} <{}> Escribió: {}".format(name, email, content),
                "correodeempresa@dominoempresa.com",
                reply_to=[email]

            )
            try:
                email.send()
            except:
                return redirect(reverse('contact')+"?fail")
            return redirect(reverse('contact')+"?ok")
    return render(request, template, {'form':form })


