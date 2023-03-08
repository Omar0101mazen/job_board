from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('',views.home, name='home'),
    path('jobs/',views.job_list, name='list'),
    path('<str:slug>',views.job_detail, name='job_detail'),

]
