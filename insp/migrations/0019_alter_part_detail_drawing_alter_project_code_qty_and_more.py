# Generated by Django 4.1.7 on 2023-12-05 01:12

from django.db import migrations, models
import insp.models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0018_part_detail_project_code_part_no_alter_check_part_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part_detail',
            name='Drawing',
            field=models.FileField(blank=True, max_length=256, null=True, upload_to=insp.models.Part_detail.get_upload_path),
        ),
        migrations.AlterField(
            model_name='project_code',
            name='Qty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project_code',
            name='Work_order_No',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
