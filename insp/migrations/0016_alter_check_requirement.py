# Generated by Django 4.1.7 on 2023-11-29 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0015_alter_check_requirement_alter_check_spec_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='Requirement',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]