# Generated by Django 4.0.4 on 2022-07-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_alter_categoria_options_alter_publicacion_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='main_image',
            field=models.ImageField(blank=True, default='post-image-default-2.png', null=True, upload_to='post_image'),
        ),
    ]
