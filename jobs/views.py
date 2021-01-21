from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Jobs

def dashboard_view(request,*args, **kwargs):
    return render(request,"main.html",context={},status=200)


def home_view(request,*args, **kwargs):
    return render(request,"pages/AllJobs.html",context={},status=200)

#REST API VIEW #Consumed by JS or Swift/Java/iOS/Android #return JSON Data

def jobs_list_view(request, *args, **kwargs):
    qs = Jobs.objects.all()
    jobsList = [{"id":x.id,"description":x.description} for x in qs]
    data = {
        "response":jobsList,
        
    }
    return JsonResponse(data)

def jobs_view_detail(request, jobs_id,*args, **kwargs):
    data = {
        "id":jobs_id,
        #"img_path":obj.image.url,
    }
    status = 200
    try:
        obj = Jobs.objects.get(id=jobs_id)
        data['description'] = obj.description
    except:
        data['description'] = "Job Not Found"
        status = 404
    return JsonResponse(data,status=status)