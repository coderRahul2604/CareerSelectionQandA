# Generated by Django 4.1.4 on 2023-04-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0002_dislike_add_time_like_add_time_alter_dislike_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
