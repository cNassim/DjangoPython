# Generated by Django 5.0.6 on 2024-06-05 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidature',
            fields=[
                ('id_candidature', models.AutoField(primary_key=True, serialize=False)),
                ('id_etudiant', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=500)),
                ('Date_de_naissance', models.DateField()),
                ('Nationalité', models.CharField(max_length=50)),
                ('CIN', models.CharField(max_length=50)),
                ('Date_de_soumission', models.DateTimeField(auto_now_add=True)),
                ('Lettre_de_motivation', models.CharField(max_length=50)),
                ('BAC', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('note_BAC', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('universite1', models.CharField(blank=True, max_length=250, null=True)),
                ('formation1', models.CharField(blank=True, max_length=250, null=True)),
                ('universite2', models.CharField(blank=True, max_length=250, null=True)),
                ('formation2', models.CharField(blank=True, max_length=250, null=True)),
                ('universite3', models.CharField(blank=True, max_length=250, null=True)),
                ('formation3', models.CharField(blank=True, max_length=250, null=True)),
                ('universite4', models.CharField(blank=True, max_length=250, null=True)),
                ('formation4', models.CharField(blank=True, max_length=250, null=True)),
                ('universite5', models.CharField(blank=True, max_length=250, null=True)),
                ('formation5', models.CharField(blank=True, max_length=250, null=True)),
                ('universite6', models.CharField(blank=True, max_length=250, null=True)),
                ('formation6', models.CharField(blank=True, max_length=250, null=True)),
                ('universite7', models.CharField(blank=True, max_length=250, null=True)),
                ('formation7', models.CharField(blank=True, max_length=250, null=True)),
                ('universite8', models.CharField(blank=True, max_length=250, null=True)),
                ('formation8', models.CharField(blank=True, max_length=250, null=True)),
                ('status1', models.CharField(default='pending', max_length=50)),
                ('status2', models.CharField(default='pending', max_length=50)),
                ('status3', models.CharField(default='pending', max_length=50)),
                ('status4', models.CharField(default='pending', max_length=50)),
                ('status5', models.CharField(default='pending', max_length=50)),
                ('status6', models.CharField(default='pending', max_length=50)),
                ('status7', models.CharField(default='pending', max_length=50)),
                ('status8', models.CharField(default='pending', max_length=50)),
                ('id_agent', models.IntegerField()),
            ],
        ),
    ]
