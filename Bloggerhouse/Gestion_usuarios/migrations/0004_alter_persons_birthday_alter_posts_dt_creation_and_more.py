# Generated by Django 4.0.4 on 2022-06-21 00:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_usuarios', '0003_alter_persons_birthday_alter_posts_dt_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2022, 6, 20, 21, 48, 33, 628607)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='dt_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 21, 48, 33, 628607)),
        ),
        migrations.AlterField(
            model_name='users',
            name='dt_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 21, 48, 33, 628607)),
        ),
        migrations.AlterField(
            model_name='users',
            name='dt_last_connection',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 21, 48, 33, 628607)),
        ),
    ]
