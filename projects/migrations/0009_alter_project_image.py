# Generated by Django 4.1.1 on 2022-09-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0008_project_input_data_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FilePathField(null=True),
        ),
    ]
