# Generated by Django 2.2.14 on 2020-07-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20200720_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(default=0, null=True),
        ),
    ]