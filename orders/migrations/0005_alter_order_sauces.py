# Generated by Django 4.0.4 on 2022-08-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sauce', '0001_initial'),
        ('orders', '0004_alter_order_sauces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sauces',
            field=models.ManyToManyField(blank=True, null=True, to='sauce.sauce'),
        ),
    ]
