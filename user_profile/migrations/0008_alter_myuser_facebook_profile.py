# Generated by Django 4.2.2 on 2023-06-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_alter_myuser_facebook_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='facebook_profile',
            field=models.CharField(),
        ),
    ]
