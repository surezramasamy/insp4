# Generated by Django 4.1.7 on 2023-11-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0005_project_code_inspection_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
