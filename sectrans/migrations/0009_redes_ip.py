# Generated by Django 5.1.2 on 2024-10-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectrans', '0008_alter_carros_serial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redes',
            name='ip',
            field=models.CharField(default='192.168.0.1', max_length=11),
        ),
    ]