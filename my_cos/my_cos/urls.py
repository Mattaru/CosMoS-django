from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('racoon_burrow/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('acc.urls')),
    path('', include('administration.urls')),
    path('', include('app.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
