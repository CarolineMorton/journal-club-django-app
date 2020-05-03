from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # example: /reviews/1/
    path('<int:review_id>/', views.write_review, name='Write Review'),
]