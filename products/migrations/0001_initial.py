# Generated by Django 5.1.3 on 2024-11-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.TextField()),
                ('image', models.FileField(upload_to='media')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
