# Generated by Django 2.2.26 on 2022-01-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imgURL',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
