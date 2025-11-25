from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        verbose_name = 'کابر'
        verbose_name_plural = 'کاربران'

    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام') 
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام خانوادگی')
    phone_number = models.IntegerField(null=True, blank=True, verbose_name='شماره تلفن')
    license = models.CharField(max_length=20, choices=[('دارد','دارد'),('ندارد','ندارد')], verbose_name='مجوز')

    def __str__(self):
        return self.username

class Donation(models.Model):
    class Meta:
        verbose_name = "کمک"
        verbose_name_plural = "کمک ها"

    class DonationType(models.TextChoices):
        CASH = ("cash", "پول نقد")
        CREDIT_CARD = ("credit_card", "کارت بانکی")
        CRYPTO = ("crypto", "رمز ارز")
        BANK_TRANSFER = ("bank transfer", "کارت به کارت")
        PAYPAL = ("PayPal", "پی پال")
        OTHER = ("other", "سایر")

    class DonorType(models.TextChoices):
        Individual = ("Individual", "شخص حقیقی") 
        Company = ("Company", "شرکت") 
        Organization = ("Organization", "سازمان")

    class AnonymizeDonation(models.TextChoices): 
        YES = ('yes','بله')
        NO = ('no','خیر')

    time_created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    time_update = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default='unknown', verbose_name='کاربر')
    donation_type = models.CharField(max_length=50, blank=False, choices=DonationType.choices, default=DonationType.CASH, verbose_name="شیوه پرداخت")
    donation_amount = models.IntegerField(null=True, blank=False, verbose_name="مقدار کمک")
    donor_type = models.CharField(max_length=20, choices=DonorType.choices, default=DonorType.Individual, verbose_name='اهدا کننده')
    message = models.TextField(null=True, verbose_name='توضیحات')
    anonymize_donation = models.BooleanField(default=AnonymizeDonation.NO, choices=AnonymizeDonation.choices, verbose_name='ناشناس')


    def __str__(self):
        return f"{self.user.username}::{self.donation_type}::{self.donation_amount}"