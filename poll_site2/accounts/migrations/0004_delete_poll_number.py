# Generated by Django 4.1 on 2022-08-28 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_poll_number"),
    ]

    operations = [
        migrations.DeleteModel(name="poll_number",),
    ]
