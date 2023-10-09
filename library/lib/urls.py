from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('mat/<str:slug>/', MATget.as_view(), name='mat'),
    path('save/', views.save, name='save')



]
