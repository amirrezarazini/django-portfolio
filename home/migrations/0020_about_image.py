# Generated by Django 5.2 on 2025-06-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_blogpostcomment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='عکس کاربری'),
        ),
    ]
