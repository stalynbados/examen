# Generated by Django 3.2.9 on 2021-11-03 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('serie', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('disponible', models.IntegerField()),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
