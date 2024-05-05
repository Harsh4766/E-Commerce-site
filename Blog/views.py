from django.shortcuts import render
from .models import blogposttt

# Create your views here.

def index(request):
    post=blogposttt.objects.all()
    return render(request,'blog/index.html',{'post':post})

def blogpost(request,id):
    cpost=blogposttt.objects.filter(post_id=id)[0]
    print(cpost)
    return render(request,'blog/blogpost.html',{'cpost':cpost})
