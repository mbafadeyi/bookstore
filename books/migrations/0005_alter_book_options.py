# Generated by Django 4.0.9 on 2023-02-16 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
