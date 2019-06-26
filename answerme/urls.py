from django.urls import path
from answerme.views import *

urlpatterns = [
    path(r'^home$', index, name='index')
]
