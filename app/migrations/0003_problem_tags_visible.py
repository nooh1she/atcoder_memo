# Generated by Django 2.2.6 on 2021-09-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210920_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='tags_visible',
            field=models.TextField(blank=True, verbose_name='タグ'),
        ),
    ]