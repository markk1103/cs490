from django.shortcuts import render, redirect
from django.http import HttpResponse
from esports_site.models import Posts
from esports_site.forms import NewPost
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q

# Allows user search
class UserSearchResults(ListView):
    model = User
    
    def get_queryset(self):
        search_query = self.request.GET.get('search')
        object_list = User.objects.filter(Q(username__icontains=search_query))
        return object_list

# Renders index page
def index(request):
    return render(request, 'index.html', {})

# Renders content to specific pages (views)
@login_required
def home(request):
    if request.method == 'POST': # If the request method is POST, it will add input data to the database
        form = NewPost(request.POST or None)
        if form.is_valid(): # If the content of the post has valid values for each field, the form will be saved to the database and redirect user back to home page
            user_form = form.save(commit=False)
            user_form.poster = request.user
            user_form.save()
        return redirect('home')
    else: # If the request method is GET, it will render the page
        all_posts = Posts.objects.all
        return render(request, 'home.html', {"all_posts": all_posts})
        
    user_search = request.get_queryset()
        

# Deletes a post based on database ID
@login_required
def delete_post(request, post_id):
    post = Posts.objects.get(pk=post_id) # Grabs the primary key of the post in the Posts database
    post.delete()
    return redirect('home')