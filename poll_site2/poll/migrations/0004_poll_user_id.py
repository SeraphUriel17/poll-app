# Generated by Django 4.1 on 2022-08-28 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("poll", "0003_alter_poll_pub_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="poll",
            name="user_id",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]