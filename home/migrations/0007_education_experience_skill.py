# Generated by Django 5.2 on 2025-05-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_about_hobbies_remove_comment_is_reply_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=255, verbose_name='دانشگاه/مدرسه')),
                ('field_of_study', models.CharField(max_length=255, verbose_name='رشته')),
                ('start_year', models.CharField(max_length=4, verbose_name='سال شروع')),
                ('end_year', models.CharField(max_length=4, verbose_name='سال پایان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان شغلی')),
                ('start_year', models.CharField(max_length=4, verbose_name='سال شروع')),
                ('end_year', models.CharField(max_length=4, verbose_name='سال پایان یا حاضر')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام مهارت')),
                ('proficiency', models.IntegerField(verbose_name='درصد مهارت')),
            ],
        ),
    ]
