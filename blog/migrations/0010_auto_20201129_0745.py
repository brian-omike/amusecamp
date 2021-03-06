# Generated by Django 3.0.2 on 2020-11-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201124_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
