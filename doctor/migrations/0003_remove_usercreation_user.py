# Generated by Django 4.0.2 on 2022-02-08 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_usercreation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercreation',
            name='user',
        ),
    ]
