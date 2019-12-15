from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerWorkers',
            fields=[
                ('manager_name', models.CharField(default='', max_length=200, verbose_name='Name')),
                ('worker_name', models.CharField(default='', max_length=200, verbose_name='Name')),
            ],
        ),
    ]
