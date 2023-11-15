from india.views import *
from django.urls import path

app_name='anything'

urlpatterns=[


    path('virat/',virat,name='virat'),
    path('iyer',iyer,name='iyer'),
]