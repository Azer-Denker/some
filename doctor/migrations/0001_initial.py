# Generated by Django 5.0.3 on 2024-05-17 12:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('CL', 'Cardiologist'), ('DL', 'Dermatologists'), ('EMC', 'Emergency Medicine Specialists'), ('IL', 'Immunologists'), ('AL', 'Anesthesiologists'), ('CRS', 'Colon and Rectal Surgeons')], default='CL', max_length=3)),
                ('address', models.TextField()),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]