# Generated by Django 4.1.7 on 2023-11-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0010_project_code_machine_project_code_operator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='Remarks',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]