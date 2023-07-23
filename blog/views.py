from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post
# Create your views here.
# posts=[{
#     'Author':'coreyMs',
#     'title':'blog part1',
#     'content':'first content',
#     'date_posted':'Aug 22,2022'

# }
# ,{
#   'Author':'jane doe',
#     'title':'blog part2',
#     'content':'second content',
#     'date_posted':'Aug 22,2022'
  
# }]
def home(request):
     context={
        ' posts':Post.objects.all()
    }
     return render(request,'blog/home.html',context)


class BlogListView(ListView):
    model = Post
    template_name='blog/home.html' #by default 'post_list.html'
    context_object_name='posts'
    ordering=['-title']

def about(request):
   
    return render(request,'blog/about.html',{'title':'About'})

# def base(request):
   
#     return render(request,'blog/base.html')    

