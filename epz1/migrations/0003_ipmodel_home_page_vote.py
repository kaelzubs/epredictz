# Generated by Django 4.1.1 on 2023-02-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("epz1", "0002_alter_home_page_options_home_page_pub_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="IpModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="home_page",
            name="vote",
            field=models.ManyToManyField(
                blank=True, related_name="post_like", to="epz1.ipmodel"
            ),
        ),
    ]
