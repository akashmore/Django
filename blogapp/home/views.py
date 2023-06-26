from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from blog.models import Blogpost
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        phone = request.POST.get("phone")
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(message)<4:
            messages.error(request,"Please fill the form correctly.")
        else:
            contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
            contact.save()
            messages.success(request,"Your message has been successfully sent.")
    return render(request,'home/contact.html')


def about(request):
    return render(request,'home/about.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Blogpost.objects.none()
    else:
        allPostsTitle= Blogpost.objects.filter(title__icontains=query)
        allPostsHead0= Blogpost.objects.filter(head0__icontains=query)
        allPostsHead1= Blogpost.objects.filter(head1__icontains=query)
        allPostsHead2= Blogpost.objects.filter(head2__icontains=query)
        allPostsChead0= Blogpost.objects.filter(chead0__icontains=query)
        allPostsChead1= Blogpost.objects.filter(chead1__icontains=query)
        allPostsChead2= Blogpost.objects.filter(chead2__icontains=query)
        allPosts=  allPostsTitle.union(allPostsHead0, allPostsHead1,allPostsHead2,allPostsChead0,allPostsChead1,allPostsChead2)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'myposts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)
    # myposts= Blogpost.objects.filter(title__icontains=query)
    # params={'myposts': myposts}
    # return render(request, 'home/search.html', params)

def handleSignUp(request):
    validate = True
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        pass1=request.POST['password']
        pass2=request.POST['repassword']

        # check for errorneous input
        if len(username)<6:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " User has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handelLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")



def handelLogout(request):
        logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('home')