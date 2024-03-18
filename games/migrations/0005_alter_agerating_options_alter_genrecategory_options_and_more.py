# Generated by Django 4.2.11 on 2024-03-18 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_genrecategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agerating',
            options={'managed': False, 'ordering': ['AgeRating_ID'], 'verbose_name': 'AgeRating', 'verbose_name_plural': 'AgeRatings'},
        ),
        migrations.AlterModelOptions(
            name='genrecategory',
            options={'managed': False, 'ordering': ['GenreCategory_ID'], 'verbose_name': 'GenreCategory', 'verbose_name_plural': 'GenreCategories'},
        ),
        migrations.AlterModelOptions(
            name='numberofplayers',
            options={'managed': False, 'ordering': ['NumberofPlayers_ID'], 'verbose_name': 'NumberofPlayers', 'verbose_name_plural': 'NumberofPlayers'},
        ),
        migrations.AlterModelOptions(
            name='popularityrating',
            options={'managed': False, 'ordering': ['PopularityRating_ID'], 'verbose_name': 'PopularityRating', 'verbose_name_plural': 'PopularityRatings'},
        ),
    ]
