# Generated by Django 4.2.5 on 2023-09-19 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='context',
            new_name='content',
        ),
    ]
