from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import home  # ← استدعاء دالة home لعرض home.html
from store.views import home  # ← استدعاء دالة home لعرض home.html


urlpatterns = [
    path('', home, name='main_home'),  # ← عرض الصفحة الرئيسية مباشرة
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
