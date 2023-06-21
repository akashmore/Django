from django.shortcuts import render,HttpResponse
from .models import Blogpost

# Create your views here.
def blogHome(request):
    myposts= Blogpost.objects.all()
    return render(request,'blog/blogHome.html',{'myposts': myposts})

def blogPost(request,id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request,'blog/blogPost.html',{'post':post})
