# Generated by Django 4.1.7 on 2023-11-23 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0006_alter_inspection_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='Var_spec_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Var_spec_min',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
