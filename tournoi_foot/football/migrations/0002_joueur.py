# Generated by Django 4.2.20 on 2025-04-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('poste', models.CharField(choices=[('Gardien', 'Gardien'), ('Défenseur', 'Défenseur'), ('Milieu', 'Milieu'), ('Attaquant', 'Attaquant')], max_length=20)),
            ],
        ),
    ]
