# Generated by Django 4.0.3 on 2022-04-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('author', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
