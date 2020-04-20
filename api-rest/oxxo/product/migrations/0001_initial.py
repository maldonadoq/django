# Generated by Django 3.0.5 on 2020-04-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=40)),
                ('alcohol', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ml', models.IntegerField()),
                ('handmade', models.BooleanField()),
                ('nationality', models.CharField(blank=True, max_length=40, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
    ]