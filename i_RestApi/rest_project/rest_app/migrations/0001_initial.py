# Generated by Django 5.1.4 on 2024-12-17 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "bookno",
                    models.CharField(
                        db_column="bookNo",
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "bookname",
                    models.CharField(
                        blank=True, db_column="bookName", max_length=30, null=True
                    ),
                ),
                (
                    "bookauthor",
                    models.CharField(
                        blank=True, db_column="bookAuthor", max_length=30, null=True
                    ),
                ),
                (
                    "bookprice",
                    models.IntegerField(blank=True, db_column="bookPrice", null=True),
                ),
                (
                    "bookdate",
                    models.CharField(
                        blank=True, db_column="bookDate", max_length=30, null=True
                    ),
                ),
                (
                    "bookstock",
                    models.IntegerField(blank=True, db_column="bookStock", null=True),
                ),
            ],
            options={
                "db_table": "book",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "pubno",
                    models.CharField(
                        db_column="pubNo",
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "pubname",
                    models.CharField(
                        blank=True, db_column="pubName", max_length=300, null=True
                    ),
                ),
            ],
            options={
                "db_table": "publisher",
                "managed": False,
            },
        ),
    ]
