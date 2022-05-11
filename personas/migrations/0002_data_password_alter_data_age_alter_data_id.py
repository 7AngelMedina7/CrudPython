# Generated by Django 4.0.4 on 2022-05-10 23:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.CharField(auto_created=True, max_length=6, primary_key=True, serialize=False),
        ),
    ]
