# Generated by Django 2.1.1 on 2018-09-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0007_nurse_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='associated_activations',
            field=models.ManyToManyField(blank=True, null=True, related_name='assoc_activations', to='activation.Activation_Message'),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='associated_responses',
            field=models.ManyToManyField(blank=True, null=True, related_name='assoc_responses', to='activation.Response_Message'),
        ),
    ]
