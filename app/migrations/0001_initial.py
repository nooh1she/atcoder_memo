# Generated by Django 2.2.5 on 2021-09-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='問題')),
                ('site_url', models.URLField(verbose_name='URL')),
                ('tag', models.CharField(max_length=50, verbose_name='タグ')),
                ('code', models.TextField(blank=True, verbose_name='自分の書いたコード')),
                ('memo', models.TextField(blank=True, verbose_name='メモ')),
            ],
        ),
    ]