# Generated by Django 4.0 on 2022-02-24 18:11

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvitedPerson',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdef1234567890', length=4, max_length=8, prefix='', primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('visit_count', models.IntegerField(default=0)),
            ],
        ),
    ]
