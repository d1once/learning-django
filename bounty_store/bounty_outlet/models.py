from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "State Entries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    country = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.street} {self.country}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Benefactor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()


class Bounty(models.Model):
    name = models.CharField(max_length=30)
    reward = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(1000)])
    benefactor = models.ForeignKey(
        Benefactor, on_delete=models.CASCADE, null=True)
    deadoralive = models.BooleanField(default=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(State)

    def get_absolute_url(self):
        return reverse("bounty-detail", args=[self.slug])

    def __str__(self) -> str:
        return f"{self.name} {self.benefactor} {self.deadoralive} ({self.reward})"
