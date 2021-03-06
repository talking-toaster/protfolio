# Generated by Django 2.2.4 on 2019-09-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='标题', max_length=50),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='摘要', max_length=50),
        ),
    ]
