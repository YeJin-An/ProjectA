# Generated by Django 4.0.1 on 2022-02-25 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.TextField()),
                ('address', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=11)),
            ],
        ),
    ]
