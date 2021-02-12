from django.urls import path
from . import views

# name of my app
app_name = 'job'

urlpatterns = [
    path('', views.job_list),
    # name=" " the name will called in (Html) files
    path('<int:id>', views.job_detail, name='job_detail') 
]