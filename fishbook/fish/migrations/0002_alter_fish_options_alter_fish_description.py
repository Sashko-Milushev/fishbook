# Generated by Django 4.1.3 on 2022-12-06 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fish',
            options={'verbose_name_plural': 'Fish'},
        ),
        migrations.AlterField(
            model_name='fish',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
