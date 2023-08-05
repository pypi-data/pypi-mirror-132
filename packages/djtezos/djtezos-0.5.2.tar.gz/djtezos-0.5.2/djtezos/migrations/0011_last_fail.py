# Generated by Django 3.2 on 2021-06-06 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djtezos', '0010_levels'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='last_fail',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions_sent', to='djtezos.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='state',
            field=models.CharField(choices=[('held', 'Held'), ('aborted', 'Aborted'), ('deploy', 'To deploy'), ('deploying', 'Deploying'), ('retrying', 'Retrying'), ('watch', 'To watch'), ('watching', 'Watching'), ('done', 'Finished')], db_index=True, default='held', max_length=200),
        ),
    ]
