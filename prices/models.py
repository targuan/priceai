from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    packaging = models.CharField(max_length=100, help_text="Ex: 500g, 1L, 1U")

    class Meta:
        ordering = ['name', 'brand']

    def __str__(self):
        return f"{self.name} ({self.brand.name}) - {self.packaging}"


class Store(models.Model):
    STORE_TYPES = [
        ('supermarket', 'Supermarché'),
        ('market', 'Marché'),
    ]

    name = models.CharField(max_length=200)
    store_type = models.CharField(max_length=20, choices=STORE_TYPES)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Magasin / Marché"
        verbose_name_plural = "Magasins / Marchés"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.get_store_type_display()})"


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='prices')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.product} - {self.amount}€"