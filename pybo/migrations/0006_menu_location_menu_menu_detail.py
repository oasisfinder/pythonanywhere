# Generated by Django 4.0.3 on 2024-08-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_alter_menu_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_detail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
