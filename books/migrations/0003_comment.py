# Generated by Django 2.1 on 2019-04-13 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_author_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=100)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Book')),
            ],
        ),
    ]
