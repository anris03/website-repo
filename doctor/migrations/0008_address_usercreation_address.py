# Generated by Django 4.0.2 on 2022-02-08 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='usercreation',
            name='address',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='doctor.address'),
        ),
    ]
