# Generated by Django 2.0.2 on 2018-02-28 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='书名')),
                ('image', models.ImageField(upload_to='books/%Y/%m/', verbose_name='封面')),
                ('author', models.CharField(max_length=100, verbose_name='作者')),
                ('translator', models.CharField(max_length=100, verbose_name='译者')),
                ('press', models.CharField(max_length=50, verbose_name='出版社')),
                ('revision', models.PositiveSmallIntegerField(verbose_name='版次')),
                ('publication_date', models.DateField(auto_now_add=True, verbose_name='出版日期')),
                ('page_numbers', models.PositiveSmallIntegerField(verbose_name='页数')),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='定价')),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='折后价')),
                ('discount', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='折扣')),
                ('stock', models.PositiveIntegerField(verbose_name='存货量')),
                ('sales', models.PositiveIntegerField(verbose_name='销售量')),
                ('introduction', models.TextField(verbose_name='介绍')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=1, verbose_name='评分')),
                ('content', models.CharField(max_length=200, verbose_name='评论')),
                ('publication_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
