from django.db.models import *
from shortuuid.django_fields import ShortUUIDField

class InvitedPerson(Model):
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
    name = CharField(max_length=100)
    sex = CharField(max_length=1, choices=SEX_CHOICES)
    description = TextField()
    visit_count = IntegerField(default=0)
    decision = BooleanField(null=True)