# Generated by Django 3.2.15 on 2023-08-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_alter_message_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
