# Generated by Django 2.2.6 on 2019-10-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_pokemon_next_evolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]