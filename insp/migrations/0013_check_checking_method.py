# Generated by Django 4.1.7 on 2023-11-29 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0012_part_group_part_part_no_part_part_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='checking_method',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
