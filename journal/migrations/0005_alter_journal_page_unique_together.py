# Generated by Django 3.2.5 on 2021-08-27 01:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0004_journal_page_stress_rating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='journal_page',
            unique_together={('author', 'pub_date')},
        ),
    ]
