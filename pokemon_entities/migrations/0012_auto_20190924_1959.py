# Generated by Django 2.2.5 on 2019-09-24 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20190924_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='next_evolution',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.Pokemon', verbose_name='Из кого эволюционировал'),
        ),
    ]