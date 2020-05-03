# Create your views here.

from django.http import HttpResponse

## views 
def index(request):
    return HttpResponse("Hello, world. You're at the journal club index.")