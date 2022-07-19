# Generated by Django 4.0.5 on 2022-07-04 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0009_dish_category_en_dish_category_ru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='category_ru',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='cooking_time_en',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='cooking_time_ru',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='recipe_en',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='recipe_ru',
        ),
    ]
