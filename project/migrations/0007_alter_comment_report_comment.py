# Generated by Django 4.2.2 on 2023-06-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_image_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='report_comment',
            field=models.BooleanField(default=False),
        ),
    ]