# Generated by Django 3.2 on 2021-06-23 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deme', '0002_auto_20210623_1717'),
        ('djago', '0006_alter_projet_date_pub'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='Investisseurs',
            field=models.ManyToManyField(related_name='_djago_projet_Investisseurs_+', through='deme.Financement', to='djago.Utilisateur'),
        ),
        migrations.AddField(
            model_name='projet',
            name='donateurs',
            field=models.ManyToManyField(related_name='_djago_projet_donateurs_+', through='deme.Don', to='djago.Utilisateur'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='compte',
            name='adresse_banque',
            field=models.CharField(max_length=20, verbose_name='Adresse de la banque'),
        ),
        migrations.AlterField(
            model_name='compte',
            name='nom_banque',
            field=models.CharField(max_length=20, verbose_name='Nom de la Banque'),
        ),
        migrations.AlterField(
            model_name='compte',
            name='proprietaire',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.PROTECT, to='djago.utilisateur', verbose_name='+'),
        ),
        migrations.AlterField(
            model_name='compte',
            name='rib',
            field=models.CharField(max_length=24, verbose_name="Relévé d'identité banquaire"),
        ),
        migrations.AlterField(
            model_name='projet',
            name='secteur',
            field=models.CharField(max_length=50, verbose_name="Secteur d'ActivitÃ©"),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='pieceid',
            field=models.CharField(max_length=50, verbose_name="Pièce d'identité"),
        ),
    ]
