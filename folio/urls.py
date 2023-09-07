from django.urls import path
from folio.views import *

urlpatterns = [
    path('', index, name='index'),
]
