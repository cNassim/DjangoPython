# Generated by Django 4.0.3 on 2024-05-31 18:14

from django.db import migrations, models


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
                ('Telephone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Candidature',
            fields=[
                ('id_candidature', models.AutoField(primary_key=True, serialize=False)),
                ('id_etudiant', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='pic/')),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Date_de_naissance', models.DateField()),
                ('Nationalité', models.CharField(max_length=50)),
                ('CIN', models.CharField(max_length=50)),
                ('Date_de_soumission', models.DateTimeField()),
                ('Lettre_de_motivation', models.CharField(max_length=50)),
                ('BAC', models.ImageField(blank=True, null=True, upload_to='doc/')),
                ('note_BAC', models.ImageField(blank=True, null=True, upload_to='doc/')),
                ('universite1', models.CharField(max_length=250)),
                ('universite2', models.CharField(max_length=250)),
                ('formation2', models.CharField(max_length=250)),
                ('universite3', models.CharField(max_length=250)),
                ('universite4', models.CharField(max_length=250)),
                ('formation4', models.CharField(max_length=250)),
                ('universite5', models.CharField(max_length=250)),
                ('universite6', models.CharField(max_length=250)),
                ('universite7', models.CharField(max_length=250)),
                ('formation7', models.CharField(max_length=200)),
                ('universite8', models.CharField(max_length=200)),
                ('formation8', models.CharField(max_length=200)),
                ('status1', models.CharField(blank=True, max_length=50, null=True)),
                ('status2', models.CharField(blank=True, max_length=50, null=True)),
                ('status3', models.CharField(blank=True, max_length=50, null=True)),
                ('status4', models.CharField(blank=True, max_length=50, null=True)),
                ('status5', models.CharField(blank=True, max_length=50, null=True)),
                ('status6', models.CharField(blank=True, max_length=50, null=True)),
                ('status7', models.CharField(blank=True, max_length=50, null=True)),
                ('status8', models.CharField(blank=True, max_length=50, null=True)),
                ('id_agent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id_formation', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
                ('id_université', models.IntegerField()),
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
                ('pays', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='univers_photos/')),
                ('siteweb', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
