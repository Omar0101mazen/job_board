from django.urls import reverse
from django.shortcuts import render,redirect
from .models import job,Category
from django.core.paginator import Paginator
from .form import apply_form
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from django.db.models import Count
# Create your views here.
def home(request):
    
    joblist = Category.objects.annotate(total_jobs =Count('job'))
    joblisttow = job.objects.all()
    myffilter = JobFilter(request.GET,queryset=joblisttow)
    joblisttow = myffilter.qs
    context ={'jobb':joblist,'num':joblisttow,'myffilter':myffilter}

    return render(request,'job/index.html',context)

def job_list(request):
    job_list = job.objects.all()
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs
    
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs':page_obj, 'myfilter' : myfilter}
    return render(request,'job/job_list.html',context)

@login_required
def job_detail(request,slug):
    job_detail = job.objects.get(slug=slug)
    if request.method == 'POST':
        form = apply_form(request.POST,request.FILES)
        if form.is_valid:
            my_form = form.save(commit=False)
            my_form.titl = job_detail
            my_form.save()
           
            
            
    else :
        form = apply_form()
        
    context = {'job':job_detail,'form':form}
    return render(request,'job/job_detail.html',context)

