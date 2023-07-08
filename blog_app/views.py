from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import user_form,post_form
from .models import user_model,post_model,User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
import datetime

# Create your views here.
def index(request):
    models=post_model.objects.all()
    umodel=User.objects.all()
    model=[]
    for i in models:
        model=[i]+model
    return render(request,'index.html',{'model':model,'umodel':umodel})

def createaccount(request):
    if request.method == 'POST':
        user_form1=user_form(request.POST)
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            if user_form1.is_valid():
                form=user_form1.save()
                form.set_password(form.password)
                form.save()
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username,password=password)
                if user:
                    if user.is_active:
                        login(request,user)
                        # formB.key = request.user
                        # formB.formA=formA
                        # formB.save()
                        return HttpResponseRedirect(reverse('blog_app:index'))
        else:
            return HttpResponse("Confirm Password didn't Match")
    else:
        user_form1=user_form()
    return render(request,'createaccount.html',{'user_form':user_form1})

def createpost(request):
    if request.method == 'POST':
        form=post_form(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.date = datetime.datetime.now()
            instance.save()
        return redirect('blog_app:index')
    return render(request,'createpost.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            print(user)
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('blog_app:index'))
            else:
                return HttpResponse('User Not Active')
        else:
            return HttpResponse('Incorret Creds')

    return render(request,'login.html',)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog_app:index'))

def myprofile(request):
    models=post_model.objects.all().filter(user=request.user)
    model=[]
    for i in models:
        model=[i]+model
    return render(request,'myprofile.html',{'model':model})

def editpost(request,id):
    ed=post_model.objects.get(id=id)
    details={
        'image':ed.image,
        'description':ed.description
    }
    if request.method == 'POST':
        form = post_form(request.POST)
        if form.is_valid():
            post_model.objects.filter(id=id).update(description=form.cleaned_data['description'])
            return redirect('blog_app:index')
    return render(request,'editpost.html',{'details':details,'ed':ed})

def deletepost(request,id):
    post=post_model.objects.get(id=id)
    post.delete()
    return redirect('blog_app:index')