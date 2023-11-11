from django.db.models import (
    Model,
    AutoField,
    CharField,
    PositiveIntegerField,
    FloatField,
)

class Product(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    price = PositiveIntegerField(default=0)
    discount_rate = FloatField(default=0)

    class Meta:
        db_table = 'products'