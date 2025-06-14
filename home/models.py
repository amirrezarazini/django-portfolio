from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Hobby(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    icon = models.ImageField(upload_to='hobbies/icons/', verbose_name='ایکون', null=True, blank=True)
    description = models.TextField(max_length=100, verbose_name='توضیحات', null=True, blank=True)

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی‌ها'

    def __str__(self):
        return self.title


class About(models.Model):
    image = models.ImageField(upload_to='media/', verbose_name='عکس کاربری', null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name='عنوان')
    profession = models.CharField(max_length=300, verbose_name='حرفه')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='تلفن')
    birthday = models.DateField(verbose_name='تولد')
    location = models.CharField(max_length=300, verbose_name='مکان تولد')
    about_me = models.TextField(verbose_name='درباره من')

    class Meta:
        verbose_name = 'اطلاعات'
        verbose_name_plural = 'اطلاعات'

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='posts')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', unique=True)
    body = models.TextField(verbose_name='متن')
    is_published = models.BooleanField(default=False, verbose_name='انتشار')
    poster = models.ImageField(upload_to='%Y/%m/%d/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='بروزرسانی')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست‌ها'

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='about_comments/', null=True, blank=True, verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'دیدگاه درباره من'
        verbose_name_plural = 'دیدگاه‌های درباره من'

    def __str__(self):
        return f"{self.user.username} - {self.body[:20]}"


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="تصویر")
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = "پست وبلاگ"
        verbose_name_plural = "پست‌های وبلاگ"

    def __str__(self):
        return self.title


class BlogPostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments', verbose_name='پست وبلاگ')
    body = models.TextField(verbose_name='متن')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE,
                               verbose_name='کامنت والد')
    likes = models.ManyToManyField(User, blank=True, related_name='liked_blogpost_comments', verbose_name='لایک‌ها')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='بروزرسانی')

    class Meta:
        verbose_name = "کامنت پست ها"
        verbose_name_plural = "کامنت پست ها"

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user.username} - {self.body[:20]}"


class Education(models.Model):
    school = models.CharField(max_length=255, verbose_name='دانشگاه/مدرسه')
    field_of_study = models.CharField(max_length=255, verbose_name='رشته')
    start_year = models.CharField(max_length=4, verbose_name='سال شروع')
    end_year = models.CharField(max_length=4, verbose_name='سال پایان')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'تحصیلات'
        verbose_name_plural = 'تحصیلات'

    def __str__(self):
        return f"{self.school} ({self.start_year} - {self.end_year})"


class Experience(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان شغلی')
    start_year = models.CharField(max_length=4, verbose_name='سال شروع')
    end_year = models.CharField(max_length=4, verbose_name='سال پایان یا حاضر')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'سابقه کاری'
        verbose_name_plural = 'سابقه‌های کاری'

    def __str__(self):
        return f"{self.title} ({self.start_year} - {self.end_year})"


class Skill(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام مهارت')
    proficiency = models.IntegerField(verbose_name='درصد مهارت')

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت‌ها'

    def __str__(self):
        return f"{self.name} - {self.proficiency}%"


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام دسته‌بندی')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='works/', verbose_name='تصویر')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته‌بندی')

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها'

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
