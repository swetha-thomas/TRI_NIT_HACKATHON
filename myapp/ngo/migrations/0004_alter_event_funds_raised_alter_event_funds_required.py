# Generated by Django 4.1.6 on 2023-02-12 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0003_rename_fund_raised_event_funds_raised_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='funds_raised',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='funds_required',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
