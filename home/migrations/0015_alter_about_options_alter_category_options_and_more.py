# Generated by Django 5.2 on 2025-05-20 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_comment_likes_remove_comment_parent_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'اطلاعات', 'verbose_name_plural': 'اطلاعات ها'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'دیدگاه', 'verbose_name_plural': 'دیدگاها'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'تحصیلات', 'verbose_name_plural': 'تحصیلات ها'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'سابقه کاری', 'verbose_name_plural': 'سابقه های کاری'},
        ),
        migrations.AlterModelOptions(
            name='hobby',
            options={'verbose_name': 'ویژگی', 'verbose_name_plural': 'ویژگی ها'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.AlterModelOptions(
            name='postcomment',
            options={'verbose_name': 'دیدگاه(2)', 'verbose_name_plural': 'دیدگاها(2)'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'مهارت', 'verbose_name_plural': 'مهارت ها'},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'نمونه کار', 'verbose_name_plural': 'نمونه کارها'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
