# Generated by Django 2.1 on 2019-04-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('auth_name', models.CharField(max_length=100)),
                ('auth_ID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
