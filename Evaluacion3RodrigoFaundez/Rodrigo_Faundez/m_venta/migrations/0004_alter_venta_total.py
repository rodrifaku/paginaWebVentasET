# Generated by Django 4.2.2 on 2023-06-24 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_venta', '0003_alter_producto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]
