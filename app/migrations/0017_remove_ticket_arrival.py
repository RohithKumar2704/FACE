# Generated by Django 4.0.2 on 2022-03-09 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='arrival',
        ),
    ]