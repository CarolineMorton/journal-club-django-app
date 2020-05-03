# Create your views here.

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render


from .models import Article_Review

## views 
def index(request):
    latest_review_list = Article_Review.objects.order_by('-review_date')[:5]
    template = loader.get_template('reviews/index.html')
    context = {
        'latest_review_list': latest_review_list,
    }
    return render(request, 'reviews/index.html', context)

def read_review(request, review_id):
    try:
        review = Article_Review.objects.get(pk=review_id)
    except Article_Review.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'reviews/review.html', {'review': review})