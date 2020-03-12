from django.shortcuts import reverse

from django.db import models

from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from mysite import settings


class CustomUser(AbstractUser):
    avatar = models.ImageField(_('Фотография'), upload_to='image/%Y/%m/%d/', blank=True, max_length=1000)
    birthday = models.DateField(_('День рождения'),blank=True, null=True)
    objects = UserManager()

    def create_custom_user(sender, instance, created, **kwargs):
        if created:
            values = {}
            for field in sender._meta.local_fields:
                values[field.attname] = getattr(instance, field.attname)
            user = CustomUser(**values)
            user.save()

    post_save.connect(create_custom_user, User)
    class Meta:
        ordering = ['username']
class Post(models.Model):
    title = models.CharField(_('Заголовок'),max_length=100,blank=False,db_index=True)
    body = models.TextField(_('Содержание'),max_length=500,blank=False,db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Объявление"
        ordering = ['-date_pub']
    def __str__(self):
        return self.title

class Comments(models.Model):
    body = models.TextField(_('Содержание'),max_length=350)
    comment_author = models.ForeignKey(CustomUser,related_name='author_comments',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date_pub']
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': str(self.post.pk)})

    def __str__(self):
        return self.body