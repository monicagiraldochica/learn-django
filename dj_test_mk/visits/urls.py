from django.urls import path
from . import views

app_name = 'visits'
urlpatterns = [
    # When someone goes to the site, if they're at the root, it will go to index without a page parameter
    path('', views.index, name='index'),
    # If they go to any other end point, it will go to index and the other part of the end point will be passed as a page parameter
    # Use <> to capture URL arguments and pass them to view
    # Arguments are strings by default, but you can specify the type. Here's we're specifying it's a string.
    path('<str:page>', views.index, name='index')
]