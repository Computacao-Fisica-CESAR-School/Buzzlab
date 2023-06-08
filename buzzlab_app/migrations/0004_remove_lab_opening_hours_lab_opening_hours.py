# Generated by Django 4.2 on 2023-05-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buzzlab_app', '0003_openinghours_is_closed_alter_address_additional_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='opening_hours',
        ),
        migrations.AddField(
            model_name='lab',
            name='opening_hours',
            field=models.ManyToManyField(to='buzzlab_app.openinghours'),
        ),
    ]