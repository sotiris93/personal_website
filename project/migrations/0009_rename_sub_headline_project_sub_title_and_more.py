# Generated by Django 4.0.6 on 2022-07-14 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_rename_post_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='sub_headline',
            new_name='sub_title',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='headline',
            new_name='title',
        ),
    ]