# Generated by Django 5.0 on 2023-12-19 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_rename_link_links_rename_click_links_clicks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]
