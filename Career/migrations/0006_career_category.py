# Generated by Django 4.1.4 on 2023-01-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Career', '0005_alter_career_cdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='category',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
