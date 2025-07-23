from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import home  # ← استدعاء الصفحة الرئيسية

urlpatterns = [
    path('', home, name='main_home'),                # الصفحة الرئيسية
    path('admin/', admin.site.urls),                 # لوحة التحكم
    path('store/', include('store.urls')),           # مسارات المتجر
    path('dashboard/', include('dashboard.urls')),   # مسارات لوحة التحكم
    path('accounts/', include('accounts.urls')),     # مسارات الحسابات
]

# دعم ملفات media و static أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
