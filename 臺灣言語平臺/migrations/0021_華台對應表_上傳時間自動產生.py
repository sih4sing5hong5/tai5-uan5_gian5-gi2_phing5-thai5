# Generated by Django 2.1.7 on 2019-02-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('臺灣言語平臺', '0020_華台對應表_文本表'),
    ]

    operations = [
        migrations.AlterField(
            model_name='華台對應表',
            name='上傳時間',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
