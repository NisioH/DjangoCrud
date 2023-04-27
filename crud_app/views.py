from django.shortcuts import render
from crud_app.models import Posts

# Create your views here.
def post_list(request):
    tamplate_name = 'post_list.html'
    posts = Posts.objects.all() # query para todas as postagens
    context = {
        'posts': posts
    }
    return render(request, tamplate_name, context)
