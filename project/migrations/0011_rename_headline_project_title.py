# Generated by Django 4.0.6 on 2022-07-19 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_rename_title_project_headline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='headline',
            new_name='title',
        ),
    ]