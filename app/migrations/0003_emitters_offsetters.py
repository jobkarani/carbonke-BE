# Generated by Django 4.1.2 on 2023-04-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_project_thememethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emitters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=256, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('more_projects', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offsetters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=256, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('more_projects', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
