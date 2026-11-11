from django.core.validators import MinValueValidator
from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Oluvchi(TimeStampedModel):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveIntegerField(default=18)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.ism

class Sotuvchi(TimeStampedModel):
    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    email = models.EmailField()
    yosh = models.PositiveIntegerField(validators=[MinValueValidator(16)])
    def __str__(self):
        return f"{self.ism} - {self.email}"

class Mahsulot(TimeStampedModel):
    nom = models.CharField(max_length=50)
    narh = models.DecimalField(max_digits=8, decimal_places=2)
    ranglar = (
        ("oq", "oq"),
        ("qizil", "qizil"),
        ("sariq", "sariq"),
    )
    rang = models.CharField(max_length=50, choices=ranglar, default="oq")
    oluvchi = models.ForeignKey(Oluvchi, on_delete=models.CASCADE)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)
