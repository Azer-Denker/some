# Generated by Django 5.0.3 on 2024-05-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_doctor_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='department',
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ManyToManyField(blank=True, default=None, related_name='adverts', to='doctor.department'),
        ),
    ]