# Generated by Django 3.1.3 on 2020-11-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='image',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]