from django.shortcuts import redirect, render
from blog.forms import BlogF
from blog.models import Blog, Category,Draft
from django.contrib import messages
from doctor.models import UserCreation
from django.contrib.auth.models import User



def blog_view(request):
    if request.method=='POST':
        try:
            if request.POST['button']=='1':
                catge=Category.objects.get(id=int(request.POST['category']))
                draft_obj=Draft(title=request.POST['title'],image=request.FILES['image'],
                                content=request.POST['content'],category=catge,user=request.user)
                draft_obj.save()
                messages.info(request,f'Saved as draft')
                return redirect('/blog/add')
        except:
            blog_objf=BlogF(request.POST,request.FILES)
            if blog_objf.is_valid():
                catger=Category.objects.get(id=int(request.POST['category']))
                summar=request.POST['content'][:200]+'...'
                blog_obj=Blog(title=request.POST['title'],image=request.FILES['image'],
                            summary=summar,content=request.POST['content'],category=catger,
                            user=request.user)
                blog_obj.save()
                return redirect('/')
                
    else:
        blog_objf=BlogF()
        stat=None
    try:
        if request.user.usercreation.choice=='1':
            stat=1
    except:
        stat=None
    return render(request,'blog/add.html',{"form":blog_objf,"status":stat})

def post_cat(request):
    return render(request,'blog/post_cat.html')

def post_details(request,pk):
    rel_blogs=Category.objects.get(pk=pk)
    stat=None
    try:
        if request.user.usercreation.choice=='2':
            stat=2
    except:
        stat=None
    return render(request,'blog/post_details.html',{"posts":rel_blogs.blog_set.all(),'status':stat})


def doc_posts(request):
    stat=None
    try:
        if request.user.usercreation.choice=='1':
            stat=1
    except:
        stat=None
    return render(request,'blog/doc_posts.html',{"status":stat})


def draft_posts(request):
    stat=None
    try:
        if request.user.usercreation.choice=='1':
            stat=1
    except:
        stat=None
    return render(request,'blog/draft.html',{"status":stat})