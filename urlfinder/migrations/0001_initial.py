# Generated by Django 3.1.6 on 2021-02-04 23:27

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('url', models.URLField(default='', primary_key=True, serialize=False)),
                ('json', jsonfield.fields.JSONField()),
            ],
        ),
    ]
