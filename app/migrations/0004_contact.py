# Generated by Django 4.1.2 on 2023-04-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_emitters_offsetters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=256, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
