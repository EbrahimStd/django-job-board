from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    # for pagin\tor in HtML
    #######
    paginator = Paginator(job_list, 1) # Show #n contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #######
    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)

def job_detail(request, id):
    job_list = Job.objects.get(id=id)
    context = {'job': job_list}
    return render(request, 'job/job_detail.html', context)
