from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckTime',
            fields=[
                ('name_text', models.CharField(default='', max_length=200, verbose_name='Name')),
                ('in_or_out', models.CharField(choices=[('in', 'checkin'), ('out', 'checkout')], max_length=20, verbose_name='Check in or out')),
                ('timestamp', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
