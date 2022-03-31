# Generated by Django 4.0.3 on 2022-03-31 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_route_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='language_code',
            field=models.CharField(choices=[('en', 'english'), ('de', 'deutsch'), ('pt', 'português'), ('es', 'español'), ('ru', 'русский')], default='en', max_length=2),
        ),
    ]
