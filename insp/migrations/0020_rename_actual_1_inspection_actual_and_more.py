# Generated by Django 4.1.7 on 2023-12-11 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0019_alter_part_detail_drawing_alter_project_code_qty_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspection',
            old_name='Actual_1',
            new_name='Actual',
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='Actual_2',
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='Actual_3',
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='Actual_4',
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='Actual_5',
        ),
    ]
