# Generated by Django 4.0.3 on 2022-03-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
