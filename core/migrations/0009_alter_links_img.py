# Generated by Django 4.1.2 on 2022-10-29 17:52

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_links_img_alter_links_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='img',
            field=models.ImageField(default='/static/img/bg-try.jpg', upload_to='core/static/links', validators=[core.validators.validate_file_size]),
        ),
    ]
