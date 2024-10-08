# Generated by Django 3.2.25 on 2024-09-29 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_customer_email', models.EmailField(max_length=254, null=True)),
                ('default_contact_number', models.CharField(max_length=20, null=True)),
                ('default_delivery_country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('default_postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('default_city', models.CharField(max_length=40, null=True)),
                ('default_address_line1', models.CharField(max_length=80, null=True)),
                ('default_address_line2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_state', models.CharField(blank=True, max_length=80, null=True)),
                ('default_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
