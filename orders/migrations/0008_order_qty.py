# Generated by Django 4.0.4 on 2022-08-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='qty',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
