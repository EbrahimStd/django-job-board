from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.jop_list), # in job page ==> show all jobs
    path('<int:id>', views.jop_details), # in specific job
]