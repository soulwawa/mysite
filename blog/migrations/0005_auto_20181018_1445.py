# Generated by Django 2.1.1 on 2018-10-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181014_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name_url',
            field=models.CharField(default='fas fa-sticky-note', max_length=50),
        ),
    ]
