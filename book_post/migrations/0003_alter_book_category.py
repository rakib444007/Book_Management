# Generated by Django 5.1.1 on 2024-11-05 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_post', '0002_rename_boocategory_book_category'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookCategory', to='category.category'),
        ),
    ]
