# Generated by Django 3.1.4 on 2020-12-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20201229_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]