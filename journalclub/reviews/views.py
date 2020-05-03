# Create your views here.

from django.http import HttpResponse

## views 
def index(request):
    return HttpResponse("Hello, world. You're at the journal club index.")

def write_review(request, review_id):
    return HttpResponse(f"This is the page to write your review {review_id}")