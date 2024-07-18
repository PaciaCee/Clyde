# Generated by Django 5.0.4 on 2024-07-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_item_description_remove_item_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='item',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='', max_length=100),
        ),
    ]