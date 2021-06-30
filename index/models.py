from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return f"{self.title}"


class Contact(models.Model):
    SOCIAL_ACCOUNT_CHOICES = [('insta', 'instagram'), ('tele', 'telegram'), ('tw', 'twitter')]
    phone_num = models.CharField('phone_num', max_length=10, blank=True)
    address = models.CharField('address', max_length=100, blank=True)
    email = models.EmailField('email')
    gender = models.CharField('socail_account ', SOCIAL_ACCOUNT_CHOICES, max_length=10, default='tele')

    def __str__(self):
        return f"user phone number {self.phone_num} with email {self.email}"


