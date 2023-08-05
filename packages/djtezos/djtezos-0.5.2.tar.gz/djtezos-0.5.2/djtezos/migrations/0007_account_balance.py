# Generated by Django 3.2 on 2021-05-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djtezos', '0006_transaction_args_mich'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=9, editable=False, max_digits=18, null=True),
        ),
    ]
