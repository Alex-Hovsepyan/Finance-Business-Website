# Generated by Django 4.2.7 on 2023-11-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('text2', models.TextField(verbose_name='Text 2')),
                ('button', models.CharField(max_length=30, verbose_name='Button')),
                ('button_link', models.URLField(verbose_name='Website Link')),
            ],
        ),
    ]
