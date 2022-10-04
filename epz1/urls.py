from django.urls import path
from .views import list_home, detail_home


urlpatterns = [

    path('', list_home, name='list_home'),
    path('<slug:slug>/', detail_home , name='detail_home')

]