# Generated by Django 5.1.1 on 2024-11-09 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_post', '0008_alter_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Category',
        ),
    ]
