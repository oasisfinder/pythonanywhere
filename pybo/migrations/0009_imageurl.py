# Generated by Django 4.0.6 on 2024-08-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_memo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=500)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
