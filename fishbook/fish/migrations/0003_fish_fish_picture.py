# Generated by Django 4.1.3 on 2022-12-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0002_alter_fish_options_alter_fish_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='fish_picture',
            field=models.URLField(default='1'),
            preserve_default=False,
        ),
    ]
