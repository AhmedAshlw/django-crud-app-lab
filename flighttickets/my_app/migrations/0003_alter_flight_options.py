# Generated by Django 5.1.1 on 2024-09-07 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0002_alter_flight_departure"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="flight",
            options={"ordering": ["-departure"]},
        ),
    ]
