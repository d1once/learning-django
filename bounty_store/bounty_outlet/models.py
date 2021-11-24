from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Bounty(models.Model):
    name = models.CharField(max_length=30)
    reward = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(1000)])
    benefactor = models.CharField(max_length=30, null=True)
    deadoralive = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("bounty-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} {self.benefactor} {self.deadoralive} ({self.reward})"
