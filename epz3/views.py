from django.shortcuts import render, redirect
from . forms import ContactForms
from django.core.mail import send_mail, get_connection
from epz7.forms import EmailSignupForm
from epz1.models import Home_Page
# Create your views here.

def list_contact(request):
    pages = Home_Page.objects.filter(
        pub_date=datetime.now()
    )
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(pub_date__icontains=query) |
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
    
        ).distinct()

    submitted = False
    if request.method == 'POST':
        form = ContactForms(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@epredictz.com'),
                ['donmart4u@gmail.com'],
                connection=con
            )
            return redirect('contact_success')
    else:
        form = ContactForms()
        if 'submitted' in request.GET:
            submitted = True

    forms = EmailSignupForm()

    return render(request, 'contact_page.html', {
        'form': form,
        'submitted': submitted,
        'forms': forms,
        'pages': pages
    })


def contact_success(request):
    pages = Home_Page.objects.filter(
        pub_date=datetime.now()
    )
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(pub_date__icontains=query) |
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
    
        ).distinct()

    forms = EmailSignupForm()

    return render(request, 'contact_success.html', {'forms': forms, 'pages': pages})



