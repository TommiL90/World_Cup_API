# Generated by Django 4.1.7 on 2023-03-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="titles",
            field=models.IntegerField(default=0, null=True),
        ),
    ]