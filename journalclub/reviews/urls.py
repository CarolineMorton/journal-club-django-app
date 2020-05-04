from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # example: /reviews/1/
    path('<int:pk>/', views.ReadReviewView.as_view(), name='review'),

    path('add/', views.ReviewCreate.as_view(), name='add-review'),
]