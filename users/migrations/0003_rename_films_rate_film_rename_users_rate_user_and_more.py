# Generated by Django 4.0.5 on 2022-06-22 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='films',
            new_name='film',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='films',
            new_name='film',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='users',
            new_name='user',
        ),
    ]