# Generated by Django 5.1.2 on 2024-10-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectrans', '0011_alter_carros_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='ip',
            field=models.CharField(max_length=20),
        ),
    ]
