# Generated by Django 4.1 on 2022-09-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0004_alter_project_image_alter_project_technology_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="authors",
            field=models.TextField(null=True),
        ),
    ]