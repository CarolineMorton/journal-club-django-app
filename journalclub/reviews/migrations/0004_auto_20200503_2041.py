# Generated by Django 3.0.5 on 2020-05-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20200503_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_review',
            name='take_home',
            field=models.CharField(default='placeholder', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article_review',
            name='clarity',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article_review',
            name='study_type',
            field=models.CharField(choices=[('COH', 'Cohort Study'), ('CSS', 'Cross-Sectional Study'), ('CC', 'Case Control Study'), ('RCT', 'Randomised Clinical Trial'), ('DSC', 'Descriptive Study'), ('NAR', 'Editorial or Narrative'), ('REV', 'Evidence Review')], max_length=3),
        ),
    ]
