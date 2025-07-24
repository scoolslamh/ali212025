from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='المستخدم',
        related_name='profile'  # يسهل الوصول عبر user.profile
    )

    # يمكن الاستغناء عن هذا الحقل إذا كنت تكتفي بـ User.email
    email = models.EmailField(
        max_length=255,
        verbose_name='البريد الإلكتروني',
        blank=True  # جعله اختياريًا لتجنب التعارض
    )

    phone = models.CharField(
        max_length=15,
        verbose_name='رقم الجوال'
    )

    address = models.CharField(
        max_length=255,
        verbose_name='العنوان',
        blank=True
    )

    def __str__(self):
        return f"الملف الشخصي لـ {self.user.username}"

    class Meta:
        verbose_name = 'الملف الشخصي'
        verbose_name_plural = 'الملفات الشخصية'
