# Generated by Django 4.1.5 on 2023-03-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_post_user_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
