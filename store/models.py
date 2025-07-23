from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم المنتج')
    description = models.TextField(verbose_name='الوصف')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    image = CloudinaryField(verbose_name='صورة المنتج', blank=True, null=True)  # ✅ تم التعديل هنا
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'منتج'
        verbose_name_plural = 'المنتجات'
