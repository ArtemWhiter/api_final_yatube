# Generated by Django 2.2.16 on 2022-03-24 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20220324_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='following',
            new_name='author',
        ),
    ]
