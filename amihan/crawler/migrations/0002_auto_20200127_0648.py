# Generated by Django 3.0 on 2020-01-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawler',
            name='email',
            field=models.EmailField(max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crawler',
            name='key',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
    ]
