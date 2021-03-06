# Generated by Django 3.2.5 on 2021-08-25 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(verbose_name='Date')),
                ('satisfaction_rating', models.IntegerField(default=0)),
                ('fitness_resp', models.TextField()),
                ('nutrition_resp', models.TextField()),
                ('productivity_resp', models.TextField()),
                ('social_resp', models.TextField()),
                ('sleep_resp', models.TextField()),
                ('extra_resp', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
