from django.shortcuts import render
from .models import Visit
from django.http import HttpRequest

# A view function always accepts an HttpRequest object
# an HttpRequest object has: user (anonymous if not authenticated), body, method (get/post), heathers, url
# A view function always returns an HttpResponse object
# an HttpResponse has: status_code, content, metadata
def index(request: HttpRequest):
    v = Visit(page="")
    if request.user.is_authenticated:
        v.username = request.user.username
    v.save()

    visitors = Visit.objects.filter(page="")
    context = {"num_visits": visitors.count()}

    return render(request, "index.html", context=context)