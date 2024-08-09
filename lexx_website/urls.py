from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from debug_toolbar.toolbar import debug_toolbar_urls


urls = i18n_patterns(
    path(settings.ADMIN_BASE_URL, admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path("", include("web.urls", namespace="web")),
)

urlpatterns = urls + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
