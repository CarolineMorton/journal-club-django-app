# Create your views here.

from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from .models import Article_Review

## views
class IndexView(generic.ListView):
    template_name = 'reviews/index.html'
    context_object_name = 'latest_review_list'

    def get_queryset(self):
        ''' returns all previous reviews'''
        return Article_Review.objects.order_by('-review_date')

class ReadReviewView(generic.DetailView):
    model = Article_Review
    template_name = 'reviews/review.html'
    context_object_name = 'review'

class ReviewCreate(CreateView):
    model = Article_Review
    fields = ['citation', 'paper_name', 'author', 'year', 'journal',
              'url', 'review_date', 'study_type', 'clarity',
              'valid_methods', 'results_importance', 'generalisability',
              'take_home']
    template_name = 'reviews/add-review.html'