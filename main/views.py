from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect to same page or thank you page

    return render(request, 'main/contact.html', {'form': form})


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def gallery(request):
    return render(request, 'main/designer_profile.html')

def services(request):
    return render(request, 'main/services.html')
