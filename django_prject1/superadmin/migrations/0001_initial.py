# Generated by Django 4.0.3 on 2024-05-30 22:22

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
                ('id_agent', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Telephone', models.CharField(default='0000000000', max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='agent_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id_pays', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Spécialité',
            fields=[
                ('id_spécialité', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Université',
            fields=[
                ('id_univ', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Numero_de_telephone', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='univers_photos/')),
                ('id_pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.pays')),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id_formation', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
                ('Prérequis', models.CharField(max_length=50)),
                ('Durée', models.DurationField()),
                ('Coût_de_formation', models.DecimalField(decimal_places=2, max_digits=10)),
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
                ('id_etudiant', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Date_de_naissance', models.DateField()),
                ('Nationalité', models.CharField(max_length=50)),
                ('CIN', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='etudiant_photos/')),
                ('id_pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.pays')),
            ],
        ),
        migrations.CreateModel(
            name='Candidature',
            fields=[
                ('id_candidature', models.AutoField(primary_key=True, serialize=False)),
                ('Date_de_soumission', models.DateTimeField()),
                ('Lettre_de_motivation', models.CharField(max_length=50)),
                ('universite1', models.CharField(max_length=50)),
                ('formation1', models.CharField(max_length=50)),
                ('universite2', models.CharField(max_length=50)),
                ('formation2', models.CharField(max_length=50)),
                ('universite3', models.CharField(max_length=50)),
                ('formation3', models.CharField(max_length=50)),
                ('universite4', models.CharField(max_length=50)),
                ('formation4', models.CharField(max_length=50)),
                ('universite5', models.CharField(max_length=50)),
                ('formation5', models.CharField(max_length=50)),
                ('universite6', models.CharField(max_length=50)),
                ('formation6', models.CharField(max_length=50)),
                ('universite7', models.CharField(max_length=50)),
                ('formation7', models.CharField(max_length=50)),
                ('universite8', models.CharField(max_length=50)),
                ('formation8', models.CharField(max_length=50)),
                ('status1', models.CharField(max_length=50)),
                ('status2', models.CharField(max_length=50)),
                ('status3', models.CharField(max_length=50)),
                ('status4', models.CharField(max_length=50)),
                ('status5', models.CharField(max_length=50)),
                ('status6', models.CharField(max_length=50)),
                ('status7', models.CharField(max_length=50)),
                ('status8', models.CharField(max_length=50)),
                ('id_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.agent')),
                ('id_etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.etudiant')),
            ],
        ),
    ]
