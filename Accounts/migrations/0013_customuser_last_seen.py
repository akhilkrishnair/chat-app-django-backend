# Generated by Django 5.0.6 on 2024-07-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0012_blacklistedtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_seen',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
