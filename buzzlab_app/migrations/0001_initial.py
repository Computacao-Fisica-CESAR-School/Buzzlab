# Generated by Django 4.2 on 2023-04-26 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=63)),
                ('state', models.CharField(max_length=63)),
                ('country', models.CharField(max_length=63)),
                ('district', models.CharField(max_length=63)),
                ('street', models.CharField(max_length=63)),
                ('street_number', models.CharField(max_length=7)),
                ('additional', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('description', models.TextField(max_length=1023)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('description', models.TextField(max_length=1023)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=127)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='buzzlab_app.address')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=16)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_trusty', models.BooleanField()),
                ('favorite_labs', models.ManyToManyField(to='buzzlab_app.lab')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LabComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buzzlab_app.component')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buzzlab_app.lab')),
            ],
        ),
        migrations.AddField(
            model_name='lab',
            name='admins',
            field=models.ManyToManyField(to='buzzlab_app.userprofile'),
        ),
        migrations.AddField(
            model_name='lab',
            name='opening_hours',
            field=models.ManyToManyField(to='buzzlab_app.openinghours'),
        ),
        migrations.AddField(
            model_name='component',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buzzlab_app.componentcategory'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1023)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buzzlab_app.component')),
            ],
        ),
    ]
