# Generated by Django 4.2.2 on 2023-06-23 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalleventa',
            options={'verbose_name_plural': 'Detalles de venta'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name_plural': 'Ventas'},
        ),
    ]