# Generated by Django 2.1.5 on 2019-02-26 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_instructor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='instructor_age',
            new_name='i_age',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='instructor_id',
            new_name='i_id',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='instructor_name',
            new_name='i_name',
        ),
    ]