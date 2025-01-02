from datetime import timedelta
from django.db.models.signals import post_save, post_delete

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'username': self.user.username})

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


class Author(models.Model):
    fullname = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.fullname}"


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.pk:
            self.book.quantity -= 1
            self.book.save()
        else:
            if self.return_date:
                self.book.quantity += 1
                self.book.save()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} return date: {self.return_date}"


@receiver(post_delete, sender=Borrow)
def borrow_post_delete(sender, instance, **kwargs):
    instance.book.quantity += 1
    instance.book.save()




@receiver(post_save, sender=Borrow)
def return_date_post_save_if_none(sender, instance, created, **kwargs):
    if instance.return_date is None:
        if created:
            instance.return_date = instance.borrowed_date + timedelta(days=15)
            instance.save()


