# Generated by Django 3.1.7 on 2021-12-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_auto_20211210_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='discord',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
