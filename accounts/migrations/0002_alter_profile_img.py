# Generated by Django 3.2.14 on 2022-10-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='img', upload_to='eazycoin/media'),
        ),
    ]
