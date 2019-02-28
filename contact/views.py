from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["raulgf0293@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
            except:
                #Algo no ha ido bien
                return redirect(reverse('contact')+"?fail")

            return redirect(reverse('contact')+"?ok")

    context = {
        'form': contact_form,
    }
    return render(request, "contact/contact.html", context)