<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_detail)
=======
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.jop_list), # in job page ==> show all jobs
    path('<int:id>', views.jop_details), # in specific job
>>>>>>> 9f27d01de65174183611be96c81acc0e8acb4aca
]