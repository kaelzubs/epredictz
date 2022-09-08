from django.shortcuts import render
from . models import Home_Page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import sitemaps
from django.urls import reverse
from django.db.models import Q
from epz7.forms import EmailSignupForm
from django.shortcuts import render
# Create your views here.
from ratelimit import limits
import requests
from pathlib import Path
import os
import dotenv # <- New

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add .env variables anywhere before SECRET_KEY
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


@limits(calls=10, period=1)
def rate_limiter():

    url = "https://daily-betting-tips.p.rapidapi.com/daily-betting-tip-api/items/daily_betting_coupons"

    querystring = {"sort":"-id"}

    headers = {
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "X-RapidAPI-Key": os.environ['DAILY_RAPIDAPI_KEY'],
        "X-RapidAPI-Host": os.environ['DAILY_RAPIDAPI_HOST']
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    arrdata = data['data']
    for dt in arrdata:
        for res in dt['coupons_list_data']:
            if not Home_Page.objects.filter(
                match_dat = res['match_date'],
                match_time = res['match_time'],
                league = res['league_name'],
                home_team = res['home_team'],
                away_team = res['away_team'],
                tip = res['game_prediction'],
                tip_odd = res['odd_value'],
                result = res['match_status']
                ).exists():
                Home_Page.objects.create(
                    match_dat = res['match_date'],
                    match_time = res['match_time'],
                    league = res['league_name'],
                    home_team = res['home_team'],
                    away_team = res['away_team'],
                    tip = res['game_prediction'],
                    tip_odd = res['odd_value'],
                    result = res['match_status']
                )
    
rate_limiter()

def list_home(request):
    pages = Home_Page.objects.all().order_by('-match_dat')
    if request.user.is_staff or request.user.is_superuser:
        pages = Home_Page.objects.all().order_by('-match_dat')

    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(match_dat__icontains=query) |
            Q(country__icontains=query) |
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



class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changfreq = 'daily'

    def items(self):
        return ['list_home']

    def location(self, item):
        return reverse(item)




def handler404(request, exception, template_name="error_404.html"):
    pages = Home_Page.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        pages = Home_Page.objects.all()

    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(match_dat__icontains=query) |
            Q(country__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
        ).distinct()

    forms = EmailSignupForm()

    response = render(request, "error_404.html", {
        'pages': pages,
        'forms': forms
    })
    response.status_code = 404
    return response


def handler500(request, template_name="error_500.html"):
    pages = Home_Page.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        pages = Home_Page.objects.all()

    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(match_dat__icontains=query) |
            Q(country__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
        ).distinct()

    forms = EmailSignupForm()

    response = render(request, "error_500.html", {
        'pages': pages,
        'forms': forms
    })
    response.status_code = 500
    return response
