from django.shortcuts import render, redirect
from . models import Home_Page, IpModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from epz7.forms import EmailSignupForm
from datetime import timedelta, datetime
from django.http import HttpResponseRedirect


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    return ip

def vote_up(request, pk):
    vote_id = request.POST.get('vote-id-up')
    post = Home_Page.objects.get(pk=vote_id)
    ip = get_client_ip(request)
    if not IpModel.objects.filter(ip=ip).exists():
        IpModel.objects.create(ip=ip)
    if post.vote_like.filter(id=IpModel.objects.get(ip=ip).id).exists():
        post.vote_like.remove(IpModel.objects.get(ip=ip))
    else:
        post.vote_like.add(IpModel.objects.get(ip=ip))

    # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def vote_down(request, pk):
    vote_id = request.POST.get('vote-id-down')
    post = Home_Page.objects.get(pk=vote_id)
    ip = get_client_ip(request)
    if not IpModel.objects.filter(ip=ip).exists():
        IpModel.objects.create(ip=ip)
    if post.vote_dislike.filter(id=IpModel.objects.get(ip=ip).id).exists():
        post.vote_dislike.remove(IpModel.objects.get(ip=ip))
    else:
        post.vote_dislike.add(IpModel.objects.get(ip=ip))

    # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def list_home(request):
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
 
    paginator = Paginator(pages, 10)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    return render(request, 'home_page.html', {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })

def list_home_today(request):
    pages = Home_Page.objects.filter(
        pub_date=datetime.now()
    )
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
    
        ).distinct()
    
    paginator = Paginator(pages, 10)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    return render(request, 'home_page.html', {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })

def list_home_yesterday(request):
    pages = Home_Page.objects.filter(
        pub_date=datetime.now() - timedelta(1)
    )
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
    
        ).distinct()
    
    paginator = Paginator(pages, 10)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    return render(request, 'home_page.html', {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })

def list_home_tomorrow(request):
    pages = Home_Page.objects.filter(
        pub_date=datetime.now() + timedelta(1)
    )
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
    
        ).distinct()
    
    paginator = Paginator(pages, 10)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    return render(request, 'home_page.html', {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })

def handler404(request, exception, template_name="error_404.html"):
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

    paginator = Paginator(pages, 10)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    response = render(request, "error_404.html", {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })
    response.status_code = 404
    return response


def handler500(request, template_name="error_500.html"):
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

    paginator = Paginator(pages, 10)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    response = render(request, "error_500.html", {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })
    response.status_code = 500
    return response


def list_all_prediction(request):
    pages = Home_Page.objects.all()
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
 
    paginator = Paginator(pages, 10)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    return render(request, 'home_page.html', {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })

