# Generated by Django 4.1 on 2022-08-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.TextField(max_length=400)),
                ('image', models.ImageField(upload_to='client/')),
            ],
        ),
    ]
