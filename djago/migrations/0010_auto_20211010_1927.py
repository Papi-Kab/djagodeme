# Generated by Django 3.2.4 on 2021-10-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djago', '0009_auto_20211006_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
