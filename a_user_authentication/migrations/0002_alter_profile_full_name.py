# Generated by Django 5.1.4 on 2024-12-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_user_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
