from django.shortcuts import render
from blog_app.models import Blog
# Create your views here.


def blog(request):
    # all_blog = Blog.objects.order_by('blog_title')
    all_blog = Blog.objects.all().order_by('-id')

    print("####################")
    print(all_blog)
    print("####################")

    diction = {'all_blog': all_blog}
    return render(request,'blog_app/blog.html', context = diction)



def blog_details(request, slug):

    # access package without loop in template
    blog = Blog.objects.get(slug=slug)

    diction = {'blog':blog}
    return render(request, 'blog_app/blog_details.html', context = diction)