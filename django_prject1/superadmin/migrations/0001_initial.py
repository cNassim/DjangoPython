# Generated by Django 4.0.3 on 2024-05-29 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id_agent', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Telephone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id_pays', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Spécialité',
            fields=[
                ('id_spécialité', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Responsable', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Université',
            fields=[
                ('id_univ', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Numero_de_telephone', models.CharField(max_length=50)),
                ('FAX', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('id_pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.pays')),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id_formation', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
                ('Prérequis', models.CharField(max_length=50)),
                ('Durée', models.TimeField()),
                ('Coût_de_formation', models.FloatField()),
                ('Langue', models.CharField(max_length=50)),
                ('Programme', models.CharField(max_length=50)),
                ('Campus', models.CharField(max_length=50)),
                ('Niveau_d_étude', models.CharField(max_length=50)),
                ('id_spécialité', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.spécialité')),
                ('id_univ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.université')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id_etudiant', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Date_de_naissance', models.CharField(max_length=50)),
                ('Nationalité', models.CharField(max_length=50)),
                ('CIN', models.CharField(max_length=50)),
                ('id_pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.pays')),
            ],
        ),
        migrations.CreateModel(
            name='Candidature',
            fields=[
                ('id_candidature', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Formation', models.CharField(max_length=50)),
                ('Université', models.CharField(max_length=50)),
                ('Spécialité', models.CharField(max_length=50)),
                ('Status', models.CharField(max_length=50)),
                ('Date_de_soumission', models.DateTimeField()),
                ('Lettre_de_motivation', models.CharField(max_length=50)),
                ('id_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.agent')),
                ('id_etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.etudiant')),
            ],
        ),
    ]