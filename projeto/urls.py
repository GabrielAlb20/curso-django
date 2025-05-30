from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# domínio/recipes/sobre
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('recipes.urls')), # /
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)