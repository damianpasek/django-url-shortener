from django.db import models
from .utils import generate_code


class ShortUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ShortUrlManager, self).all(*args, **kwargs).filter(active=True)


class ShortUrl(models.Model):
    url = models.CharField(max_length=250)
    code = models.CharField(max_length=16, unique=True, blank=True)
    active = models.BooleanField(default=True)

    objects = ShortUrlManager()

    def save(self, *args, **kwargs):
        if self.code is None or self.code == "":
            self.code = generate_code()
        super(ShortUrl, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
