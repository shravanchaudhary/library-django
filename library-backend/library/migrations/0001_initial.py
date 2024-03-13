# Generated by Django 5.0.3 on 2024-03-13 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("copies", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Circulation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("checkedout", models.BooleanField(default=True)),
                ("returned", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Members",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("fulfilled", models.BooleanField(default=False)),
            ],
        ),
        migrations.AddConstraint(
            model_name="books",
            constraint=models.UniqueConstraint(fields=("name",), name="unique_book"),
        ),
        migrations.AddField(
            model_name="circulation",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="library.books"
            ),
        ),
        migrations.AddConstraint(
            model_name="members",
            constraint=models.UniqueConstraint(fields=("name",), name="unique_member"),
        ),
        migrations.AddField(
            model_name="circulation",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="library.members"
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="library.books"
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="library.members"
            ),
        ),
        migrations.AddConstraint(
            model_name="circulation",
            constraint=models.UniqueConstraint(
                condition=models.Q(("checkedout", True)),
                fields=("book", "member", "returned", "checkedout"),
                name="unique_circulation",
            ),
        ),
        migrations.AddConstraint(
            model_name="reservation",
            constraint=models.UniqueConstraint(
                fields=("book", "member"), name="unique_reservation"
            ),
        ),
    ]
