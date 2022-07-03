# Generated by Django 4.0.1 on 2022-04-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Added_date', models.DateField(auto_now=True)),
                ('due', models.DateField(null=True)),
                ('item', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Todo',
            },
        ),
    ]
