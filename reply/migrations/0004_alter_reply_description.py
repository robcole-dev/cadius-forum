# Generated by Django 3.2.13 on 2022-07-13 08:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0003_alter_reply_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]