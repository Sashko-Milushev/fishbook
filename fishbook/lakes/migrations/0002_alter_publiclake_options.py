# Generated by Django 4.1.3 on 2023-06-27 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lakes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publiclake',
            options={'ordering': ('name',)},
        ),
    ]
