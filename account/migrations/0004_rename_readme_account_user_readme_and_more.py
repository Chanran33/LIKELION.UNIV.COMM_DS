# Generated by Django 4.0.6 on 2022-07-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_readme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='readme',
            new_name='user_readme',
        ),
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='githubName',
        ),
        migrations.AddField(
            model_name='account',
            name='github_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user_email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user_name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='account',
            table=None,
        ),
    ]
