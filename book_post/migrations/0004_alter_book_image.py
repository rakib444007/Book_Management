# Generated by Django 5.1.1 on 2024-11-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_post', '0003_alter_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_post/upload'),
        ),
    ]