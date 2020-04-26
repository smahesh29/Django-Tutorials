from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import NameForm, ContactForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            
            messages.success(request, f'Thanks!')
            return redirect('name')

    else:
        form = NameForm()

    return render(request, 'myapp/name.html', {'form': form})

def html_form(request):
    return render(request, 'myapp/form.html')

def mail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['recipients_email_address']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            messages.success(request, f'Mail has been Send!')
            return redirect('mail_form')
    else:
        form = ContactForm(request.POST)

    return render(request, 'myapp/mail.html', {'form': form})