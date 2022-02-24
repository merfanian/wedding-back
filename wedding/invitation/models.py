from django import forms
from django.db import models
from shortuuid.django_fields import ShortUUIDField

class InvitedPerson(models.Model):
    SEX_CHOICES = [
        ("m", "Male"),
        ("f", "Female"),
        ("o", "Other")
    ]

    id = ShortUUIDField(
        length=4,
        max_length=8,
        alphabet="abcdef1234567890",
        primary_key=True,
    )
    name = models.TextField()
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    description = models.TextField()
    visit_count = models.IntegerField(default=0)