from django.shortcuts import render
from . forms import ContactForm
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import get_template

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def projects(request):
    return render(request, 'projects.html')
def skills(request):
    return render(request, 'skills.html')
def resume(request):
    return render(request, 'resume.html')

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get(
                'name'
            , '')
            email = request.POST.get(
                'email'
            , '')
            response = request.POST.get('response', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'name': name,
                'email': email,
                'response': response,
            }
            content = template.render(context)

            email = EmailMessage(
                "Someone has contacted you",
                content,
                "Your website" +'',
                ['coderjaymit@gmail.com'],
                headers = {'Reply-To': email })


            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
