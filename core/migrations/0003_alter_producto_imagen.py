# Generated by Django 3.2.3 on 2021-07-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210711_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
