from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils import timezone

# Create your models here.

class Menu(models.Model):
    TYPE_CHOICES = [
        ('한식', '한식'),
        ('양식', '양식'),
        ('중식', '중식'),
        ('일식', '일식'),
        ('기타', '기타'),
        ("분식", "분식"),]

    location_CHOICES = [
        ('충정로', '충정로'),
        ('아현동', '아현동'),
        ('풍산빌딩 지하', '풍산빌딩 지하'),
        ('서대문', '서대문'),]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices = TYPE_CHOICES)
    distance = models.CharField(max_length=50)
    location = models.CharField(max_length=50, choices = location_CHOICES)
    price = models.IntegerField(null=True, blank=True)
    menu_detail = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Memo(models.Model):
    class Status(models.TextChoices):
        PENDING = '대기중', _('대기중')
        IN_PROGRESS = '진행중', _('진행중')
        COMPLETED = '완료', _('완료')

    title = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self):
        return self.title


class ImageURL(models.Model):
    url = models.URLField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.url
