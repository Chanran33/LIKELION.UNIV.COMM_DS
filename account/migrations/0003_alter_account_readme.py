# Generated by Django 4.0.6 on 2022-07-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='readme',
            field=models.TextField(null=True),
        ),
    ]
