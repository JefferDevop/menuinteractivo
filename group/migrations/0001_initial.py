# Generated by Django 4.0.4 on 2022-08-06 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sauce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('sauces', models.ManyToManyField(blank=True, to='sauce.sauce')),
            ],
        ),
    ]