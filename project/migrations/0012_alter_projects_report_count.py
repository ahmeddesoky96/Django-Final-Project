# Generated by Django 4.2.2 on 2023-06-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_report_report_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='report_count',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
