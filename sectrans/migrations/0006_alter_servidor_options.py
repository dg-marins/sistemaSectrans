# Generated by Django 5.1 on 2024-10-30 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sectrans', '0005_alter_servidor_ip_publico'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servidor',
            options={'verbose_name': 'Servidor', 'verbose_name_plural': 'Servidores'},
        ),
    ]
