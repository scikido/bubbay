# Generated by Django 4.0.3 on 2022-05-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encode', models.CharField(max_length=122, null=True)),
                ('decoded_msg', models.CharField(max_length=122, null=True)),
            ],
        ),
    ]
