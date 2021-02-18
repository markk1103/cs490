# URLs for the main site
from esports_site import views
from django.urls import path
from .views import UserSearchResults

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', UserSearchResults.as_view(template_name='search.html'), name='search'),
    path('delete/<post_id>', views.delete_post, name='delete_post'),
]
 
