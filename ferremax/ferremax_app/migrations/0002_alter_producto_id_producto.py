# Generated by Django 5.0.6 on 2024-05-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferremax_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
