# Generated by Django 2.1.1 on 2018-09-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0012_auto_20180929_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='response_message',
            name='response_message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]