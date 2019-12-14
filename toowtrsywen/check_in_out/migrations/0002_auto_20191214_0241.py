# Generated by Django 3.0 on 2019-12-14 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_in_out', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonsName',
        ),
        migrations.AddField(
            model_name='checktime',
            name='name_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='checktime',
            name='in_or_out',
            field=models.CharField(choices=[('in', 'checkin'), ('out', 'checkout')], max_length=20),
        ),
    ]