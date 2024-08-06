from django.db import models

# Create your models here.

class Menu(models.Model):
    TYPE_CHOICES = [
        ('한식', '한식'),
        ('양식', '양식'),
        ('중식', '중식'),
        ('일식', '일식'),
        ('기타', '기타'),
        ("분식", "분식"),]
    # location_CHOICES = [
    #     ('충정로', '한식'),
    #     ('아현', '양식'),
    #     ('중식', '중식'),
    #     ('일식', '일식'),
    #     ('기타', '기타'),
    #     ("분식", "분식"), ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices = TYPE_CHOICES)
    distance = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True, blank = True)
    price = models.IntegerField(null=True, blank=True)
    menu_detail = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


