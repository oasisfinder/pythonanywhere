# Generated by Django 4.0.3 on 2024-08-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_alter_menu_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='type',
            field=models.CharField(choices=[('한식', '한식'), ('양식', '양식'), ('중식', '중식'), ('일식', '일식'), ('기타', '기타'), ('분식', '분식')], max_length=50),
        ),
    ]