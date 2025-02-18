from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog

# Home page view
def hello_world(request):
    data = {
        "title": "Welcome to Django Template",
        "items": ["Python", "Django", "Templates"]
    }
    return render(request, "home.html", data)

# Simple HTTP response view
def hello_blog(request):
    return HttpResponse("Hello, This is my first blog")

def data(request):
    return HttpResponse("This is the data page.")

# List all blog posts
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})

# Blog detail view
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog_detail.html", {"blog": blog})  # Corrected key from "blogs" to "blog"

# Create a new blog post
def blog_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Blog.objects.create(title=title, content=content)
        return redirect('blog_list')  # Fixed redirect name
    return render(request, "blog_form.html")

# Delete a blog post
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('blog_list')

def product_list(request):
    products=[
        {"name":"laptop","price":"$455"},
        {"name":"Iphone", "price":"$100"}

    ]
    return render(request, "products.html",{"products":products})

