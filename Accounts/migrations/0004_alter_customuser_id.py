# Generated by Django 5.0.6 on 2024-06-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
