# Generated by Django 5.0.6 on 2024-05-31 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0002_remove_candidature_id_agent_candidature_formation3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidature',
            name='status1',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='status2',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='status3',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='status4',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='status5',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='status6',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='status7',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='status8',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
