# Generated by Django 4.0.6 on 2022-07-14 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_rename_tag_skill_rename_tags_post_skills'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post',
            new_name='Project',
        ),
    ]