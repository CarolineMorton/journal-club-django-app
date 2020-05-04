from django.db import models
from django.urls import reverse

class Article_Review(models.Model):

    Cohort = "COH"
    CrossSectional = "CSS"
    CaseControl = "CC"
    RCT = "RCT"
    Descriptive = "DSC"
    Narrative = "NAR"
    Review = "REV"

    STUDY_CHOICES = [
        (Cohort, "Cohort Study"),
        (CrossSectional, "Cross-Sectional Study"), 
        (CaseControl, "Case Control Study"), 
        (RCT, "Randomised Clinical Trial"), 
        (Descriptive, "Descriptive Study"),
        (Narrative, "Editorial or Narrative"),
        (Review, "Evidence Review") 
    ]

    citation = models.TextField()
    paper_name = models.TextField()
    author = models.CharField(max_length=1000)
    year = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

    review_date = models.DateTimeField('Date Reviewed')

    study_type = models.CharField(choices=STUDY_CHOICES, max_length=3)

    clarity = models.TextField()

    valid_methods = models.TextField()

    results_importance = models.TextField()

    generalisability = models.TextField()

    take_home = models.TextField()

    def get_absolute_url(self):
        return reverse('review', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.citation