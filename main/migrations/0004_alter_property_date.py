# Generated by Django 4.2.5 on 2023-09-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_property_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]