# Generated by Django 5.0.1 on 2024-02-06 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_user_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
    ]