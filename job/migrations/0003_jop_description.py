# Generated by Django 3.1.6 on 2021-02-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jop_jop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]