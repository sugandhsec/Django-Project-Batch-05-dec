# Generated by Django 5.0 on 2023-12-18 03:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_buyer', '0002_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200)),
                ('cdescription', models.TextField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_buyer.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='product/')),
                ('description', models.TextField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_seller.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_buyer.user')),
            ],
        ),
    ]