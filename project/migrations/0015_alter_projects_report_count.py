# Generated by Django 4.2.2 on 2023-06-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_projects_report_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='report_count',
            field=models.IntegerField(default=0),
        ),
    ]