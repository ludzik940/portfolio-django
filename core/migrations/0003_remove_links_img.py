# Generated by Django 4.1.2 on 2022-10-28 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_member_links_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='img',
        ),
    ]
