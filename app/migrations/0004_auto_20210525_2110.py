# Generated by Django 3.2.2 on 2021-05-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descrip',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(),
        ),
    ]
