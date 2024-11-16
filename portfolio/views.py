# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  # Use your actual home template


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')  # Redirect after successful form submission
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

from django.shortcuts import render

def about_view(request):
    return render(request, 'about.html')

def projects_view(request):
    return render(request, 'projects.html')  # Add this function if missing