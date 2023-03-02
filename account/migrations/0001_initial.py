# Generated by Django 4.1.7 on 2023-03-02 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='Only English letters and numbers are allowed', regex='^[a-zA-Z][a-zA-Z0-9]{6,30}$')])),
                ('email', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Your email is not valid', regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')], verbose_name='Email Address')),
                ('firstname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='The format is not valid', regex='^[a-zA-Z]{2,30}$')], verbose_name='first name')),
                ('lastname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='The format is not valid', regex='^[a-zA-Z]{2,30}$')], verbose_name='last name')),
                ('gender', models.CharField(choices=[('Mr', 'Man'), ('mrs', 'Female')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('account_creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
