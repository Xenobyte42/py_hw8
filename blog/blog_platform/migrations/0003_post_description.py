# Generated by Django 2.1.4 on 2018-12-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_platform', '0002_auto_20181210_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=50, verbose_name='Description'),
        ),
    ]