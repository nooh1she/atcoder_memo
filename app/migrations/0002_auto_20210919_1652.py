# Generated by Django 2.2.5 on 2021-09-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='tag',
        ),
        migrations.AddField(
            model_name='problem',
            name='tags',
            field=models.TextField(blank=True, verbose_name='タグ'),
        ),
    ]