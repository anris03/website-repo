# Generated by Django 4.0.2 on 2022-02-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0019_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreation',
            name='pic',
            field=models.ImageField(default='default.jpg', upload_to='uploads'),
        ),
    ]
