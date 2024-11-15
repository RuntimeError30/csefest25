# Generated by Django 5.1.3 on 2024-11-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_events_detailed_description_alter_events_eventimage_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prizemoney",
            name="fourthToTenth_prize",
        ),
        migrations.AddField(
            model_name="prizemoney",
            name="eight_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="prizemoney",
            name="fifth_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="prizemoney",
            name="fourth_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="prizemoney",
            name="nineth_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="prizemoney",
            name="seventh_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="prizemoney",
            name="sixth_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="prizemoney",
            name="tenth_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="eventrules",
            name="problem_setter",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="prizemoney",
            name="first_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="prizemoney",
            name="second_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="prizemoney",
            name="third_prize",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_01",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_02",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_03",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_04",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_05",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_06",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_07",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_08",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_09",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="timeline_10",
            field=models.CharField(default="", max_length=100),
        ),
    ]