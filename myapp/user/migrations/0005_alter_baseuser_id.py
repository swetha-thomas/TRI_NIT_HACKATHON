# Generated by Django 4.1.6 on 2023-02-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_baseuser_id_alter_ngo_primary_cause'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]