from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from .form import ApplyForm, JobForm
from .models import Job

# Create your views here.

def job_list(request):
    # all jobs in class 'Job'
    job_list = Job.objects.all()
    # for pagin\tor in HtML
    #######
    paginator = Paginator(job_list, 2) # Show #n contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #######
    context = {'jobs': page_obj}
    # to render data from DB with FrontEnd Template
    # (request, html template, context with dictionary type)
    return render(request, 'job/job_list.html', context)


def job_detail(request, id):
    # get dedails of job
    job_detail = Job.objects.get(id=id)

    # form
    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            # do not save before adding job name
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()

    else:
        form = ApplyForm()


    context = {'job': job_detail, 'form':form}
    return render(request, 'job/job_detail.html', context)

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit = False)
            myform.owner = request.user
            myform.save()
            # after save
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()

    context = {'form':form}
    return render(request, 'job/add_job.html', context)
