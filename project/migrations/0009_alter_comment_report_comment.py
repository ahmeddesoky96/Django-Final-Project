# Generated by Django 4.2.2 on 2023-06-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0008_alter_projects_report_count_report"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="report_comment",
            field=models.BooleanField(default=False),
        ),
    ]
