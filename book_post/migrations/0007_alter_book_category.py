# Generated by Django 5.1.1 on 2024-11-09 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_post', '0006_remove_book_category_book_category'),
        ('category', '0003_rename_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='BookCategory', to='category.category'),
        ),
    ]