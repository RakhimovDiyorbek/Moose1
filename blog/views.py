from operator import sub

from django.shortcuts import render, redirect
from .models import About, Blog, Home
from .forms import ContactForm, SubscriptionForms, CommentForm
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    homes = Home.objects.all()
    context = {
        'home': homes
    }
    return render(request, 'index.html', context)


def index(request):
    sub = SubscriptionForms(request.POST or None)
    if sub.is_valid():
        sub.save()
    redirect('/')
    context = {
        'subs': sub,
    }
    return render(request, "index.html", context)


def article(request):
    sub = SubscriptionForms(request.POST or None)
    if sub.is_valid():
        sub.save()
    redirect('/')
    blogs = Blog.objects.all().order_by('-id')
    p = Paginator(blogs, 3)
    page = request.GET.get('page')
    b = p.get_page(page)
    context = {
        'blogs': b,
        'subs': sub

    }
    return render(request, "blog.html", context)


class SubscriptionsForms:
    pass


def about(request):
    about = About.objects.all()
    sub = SubscriptionForms(request.POST or None)
    if sub.is_valid():
        sub.save()
    redirect('/')
    context = {
        'subs': sub,
        'abouts': about

    }
    return render(request, "about.html", context)


def contact(request):
    sub = SubscriptionForms(request.POST or None)
    if sub.is_valid():
        sub.save()
    redirect('/')
    contact = ContactForm(request.POST or None)
    if contact.is_valid():
        contact.save()
        return redirect('.')
    context = {
        'forma': contact,
        'subs': sub
    }
    return render(request, "contact.html", context)


def detail(request, pk):
    blog = Blog.objects.get(id=pk)
    comment = CommentForm(request.POST or None)
    if comment.is_valid():
        com = comment.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    context = {
        'blog': blog,
        'comment': comment
    }
    return render(request, "blog-single.html", context)
