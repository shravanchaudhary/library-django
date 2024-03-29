# Generated by Django 5.0.3 on 2024-03-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="circulation",
            name="unique_circulation",
        ),
        migrations.AddConstraint(
            model_name="circulation",
            constraint=models.UniqueConstraint(
                condition=models.Q(("checkedout", True)),
                fields=("book", "member"),
                name="unique_circulation",
            ),
        ),
    ]
