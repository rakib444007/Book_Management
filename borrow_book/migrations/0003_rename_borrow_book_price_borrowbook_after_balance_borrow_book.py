# Generated by Django 5.1.1 on 2024-11-15 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_book', '0002_rename_after_balance_borrow_book_borrowbook_borrow_book_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowbook',
            old_name='borrow_book_price',
            new_name='after_balance_borrow_book',
        ),
    ]
