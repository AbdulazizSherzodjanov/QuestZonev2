from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
def home(request):
    data = PostModel.objects.all().order_by('-id')
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home-page')
    else:
        form = PostModelForm()
        
        context = {
        'posts': data,
        'form': form
    }
    return render(request, 'home.html', context)


def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('post_detail-page', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
            'post': post,
            'c_form':c_form,
    }
    return render(request, 'post_detail.html', context)


def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail-page', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post_edit.html', context)


def post_delete(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'GET':
        post.delete()
        return redirect('home-page')
    context = {
        'post' : post
    }
    return render(request,'post_delete.html',context)


def search(request):
    if request.method == 'GET':  # agar request.methodi teng bo'lsa POSTga
        searched = request.GET['searched']
		
        news = PostModel.objects.filter(Q(title__icontains=searched) | (Q(title__icontains=searched))) # News objectlarini title boyicha filter qilish
        return render(request, 'search.html', {'searched': searched, 'news': news})
    else:  # aks xolda
        return render(request, 'search.html', {})
    
def new_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request,"Post is successfully added.")
            
            return redirect('new_post')
    else:
        form = PostModelForm()
        context = {
        'form': form,
    }
    return render(request, 'new_post.html', context)

def menu(request):
    data = PostModel.objects.all().order_by('-id')
    ctx= {
        'posts':data
    }
    return render(request,'menu.html',ctx)