# Generated by Django 4.1.4 on 2023-01-30 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Career', '0006_career_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='category',
        ),
    ]
