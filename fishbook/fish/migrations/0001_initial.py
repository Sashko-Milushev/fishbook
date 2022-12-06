# Generated by Django 4.1.3 on 2022-12-06 08:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import fishbook.core.model_mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('type', models.CharField(choices=[('predatory', 'Predatory'), ('peaceful', 'Peaceful')], max_length=9)),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('caught_by', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(fishbook.core.model_mixins.StrFromFieldMixin, models.Model),
        ),
    ]
