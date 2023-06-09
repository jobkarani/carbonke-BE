# Generated by Django 4.1.2 on 2023-03-21 14:28

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'blogcategory',
                'verbose_name_plural': 'blogcategories',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('cover', pyuploadcare.dj.models.ImageField()),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('image2', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('image3', pyuploadcare.dj.models.ImageField(blank=True, null=True)),
                ('methodologyTitle', models.CharField(max_length=200)),
                ('methodology', models.TextField(max_length=4000)),
                ('about', models.TextField(default='', max_length=4000)),
                ('location', models.CharField(max_length=200)),
                ('verifier', models.CharField(default='', max_length=200)),
                ('tag', models.CharField(max_length=200)),
                ('youtube_Video', embed_video.fields.EmbedVideoField()),
                ('webLink', models.URLField(default='')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('heading', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=1000, null=True)),
                ('tex2', models.TextField(blank=True, max_length=1000, null=True)),
                ('text3', models.TextField(blank=True, max_length=1000, null=True)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blogcategory')),
            ],
        ),
    ]
