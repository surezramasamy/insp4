# Generated by Django 4.1.7 on 2023-11-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0003_rename_actual_inspection_actual_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='Requirement',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
