# Generated by Django 2.0.2 on 2018-02-28 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20180228_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='superior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='books.Category', verbose_name='上级'),
        ),
    ]
