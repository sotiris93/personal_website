# Generated by Django 4.0.6 on 2022-07-14 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_post_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Skill',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='skills',
        ),
    ]
