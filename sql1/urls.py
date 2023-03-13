from sql1.views import *
from django.urls import path
add_name='html2'

urlpatterns=[
    path('html2/',html2,name='html2'),
]