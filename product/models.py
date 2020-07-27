from django.db import models


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=250)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        
        return self.name


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    thumbnail = models.ImageField(upload_to='images/product', default='images/not_found.jpg')
    image_1 = models.ImageField(upload_to='images/product', default='images/not_found.jpg')
    image_2 = models.ImageField(upload_to='images/product', default='images/not_found.jpg')
    image_3 = models.ImageField(upload_to='images/product', default='images/not_found.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return f'{self.name}({self.category})'

