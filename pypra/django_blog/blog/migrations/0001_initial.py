# Generated by Django 2.1.7 on 2019-07-04 05:57

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='album', verbose_name='首图')),
                ('position', models.CharField(max_length=24, verbose_name='地点')),
                ('desc', models.CharField(max_length=128, verbose_name='描述')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '相册表',
                'verbose_name_plural': '相册表',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='articles', verbose_name='首图')),
                ('title', models.CharField(max_length=24, verbose_name='标题')),
                ('desc', models.CharField(max_length=128, verbose_name='描述')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '文章表',
                'verbose_name_plural': '文章表',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='名称')),
            ],
            options={
                'verbose_name': '分类表',
                'verbose_name_plural': '分类表',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('content', models.CharField(max_length=128, verbose_name='内容')),
            ],
            options={
                'verbose_name': '留言表',
                'verbose_name_plural': '留言表',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=24, verbose_name='用户名')),
                ('password', models.CharField(max_length=72, verbose_name='密码')),
                ('avatar', models.ImageField(upload_to='avatar', verbose_name='头像')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.AddField(
            model_name='leave',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Users'),
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类'),
        ),
    ]
