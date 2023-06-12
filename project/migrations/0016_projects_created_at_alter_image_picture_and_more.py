# Generated by Django 4.2.2 on 2023-06-12 18:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_alter_projects_report_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='created_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(upload_to='static/project_pictures'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='Adminproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projects')),
            ],
        ),
    ]
