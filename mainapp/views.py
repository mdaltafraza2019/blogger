from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect,get_object_or_404
from mainapp.forms import PostForm,CategoryForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate ,login as loginfun,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(r):
    data={}
    data['post']=Post.objects.all()
    data['category']=Category.objects.all()
    return render(r,'home.html',data)



def register(r):
     form=RegisterForm(r.POST or None)
     if r.method=='POST':
          if form.is_valid():
               form.save()
               messages.success(r,'you are succesfully registered!!!')
               return redirect(login)
     return render(r,'register.html',{'form':form})

def login(r):
    form=AuthenticationForm(r.POST or None)
    if r.method=='POST':
        
          username=r.POST.get('username')
          password=r.POST.get('password')
          user=authenticate(username=username,password=password)
          if user is not None:
               if user.is_superuser:
                    return HttpResponseRedirect('/admin/')
               loginfun(r,user)
               messages.success(r,'you are succesfully loggedIn!!!')
               return redirect(home)
          else:
               messages.error(r,'invalid  username or password !!!') 
               return redirect(login)
    return render (r,'login.html',{'form':form})
def logoutfun(r):
     logout(r)
     return redirect(home)
@login_required
def addpost(r):
     data={}
     user=User
     print(user)
     categoryform=CategoryForm(r.POST or None)
     form=PostForm(r.POST or None ,r.FILES or None)
     if r.method=='POST':
          if form.is_valid():
               a=form.save(commit=False)
               a.author=r.user
               form.save()
               messages.success(r,'Post added succesfully !!!')
               return redirect(home)
     return render(r,'post.html',{'form':form,'categoryform':categoryform})
@login_required
def addcategory(r):
     categoryform=CategoryForm(r.POST or None)
     if r.method=='POST':
          if categoryform.is_valid:
               categoryform.save()
               messages.success(r,'Category added successfully!!!')
               return redirect(addpost)
     return render(r,'category.html',{'categoryform':categoryform})

def filterPost(r,id):
     data={}
     data['category']=Category.objects.all()
     data['post']=Post.objects.filter(category__id=id)

     return render(r,'home.html',data)

def searchpost(r):
     if r.method=="GET":
          data={}
          data['post']=Post.objects.filter(title__icontains=r.GET.get('search'))
          
          if data:
               return render(r,'home.html',data)
          else:
               return redirect(login)
@login_required
def mypost(r):
     user=User
     data={}
     data['post']=Post.objects.filter(author=r.user)
     
     return render(r,'mypost.html',data)

@login_required
def editpost(r,id):
     post=Post.objects.get(id=id)
     form=PostForm(r.POST or None ,r.FILES or None,instance=post)
     if r.method=='POST':
          if form.is_valid():
               form.save()
               return redirect(home)
     return render(r,'editpost.html',{'form':form})
@login_required
def deletepost(r,id):
     post=Post.objects.get(id=id)
     post.delete()
     messages.success(r,'Post deleted successfully!!!')
     return redirect(mypost)

def singlepost(r,id):
     spost=get_object_or_404(Post,id=id)
     data={
          'category':Category.objects.all(),
          'post':spost,
          'releted_post':Post.objects.filter(~Q(id=id)&Q(category__id=spost.category.id))

     }
     
     return render(r,'singlepost.html',data)