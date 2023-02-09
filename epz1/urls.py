from django.urls import path
from .views import list_home, list_home_yesterday, list_home_today, list_home_tomorrow

urlpatterns = [
    path('', list_home, name='list_home'),
    path('yesterday/', list_home_yesterday, name='list_home_yesterday'),
    path('today/', list_home_today, name='list_home_today'),
    path('tomorrow/', list_home_tomorrow, name='list_home_tomorrow')
]
