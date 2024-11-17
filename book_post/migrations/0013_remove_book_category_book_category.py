# Generated by Django 5.1.1 on 2024-11-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_post', '0012_alter_book_category'),
        ('category', '0004_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Category',
        ),
        migrations.AddField(
            model_name='book',
            name='Category',
            field=models.ManyToManyField(related_name='BookCategory', to='category.category'),
        ),
    ]
