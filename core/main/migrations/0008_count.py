# Generated by Django 4.2.7 on 2023-11-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='Number')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
            ],
        ),
    ]
