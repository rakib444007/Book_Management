# Generated by Django 5.1.1 on 2024-11-15 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowbook',
            old_name='after_balance_borrow_book',
            new_name='borrow_book_price',
        ),
        migrations.RemoveField(
            model_name='borrowbook',
            name='return_date',
        ),
    ]
