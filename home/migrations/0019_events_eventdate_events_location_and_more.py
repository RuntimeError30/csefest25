# Generated by Django 5.1.3 on 2024-11-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0018_guidelines_delete_competitionsyllabus"),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="eventDate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="events",
            name="location",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name="eventInformations",
        ),
    ]
