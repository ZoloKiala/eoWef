# Generated by Django 3.0.8 on 2021-05-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20210401_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variables',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
