# Generated by Django 4.2.9 on 2024-03-17 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_agerating_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genrecategory',
            options={'managed': False, 'ordering': ['GenreCategoryID'], 'verbose_name': 'GenreCategory', 'verbose_name_plural': 'GenreCategories'},
        ),
    ]
