from django.contrib import admin
from django.urls import include, path, re_path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # Wagtail / Peregrine URLs
    path('documents/', include(wagtaildocs_urls)),
    path('cms/', include(wagtailadmin_urls)),
    re_path(r'^', include('peregrine.urls')),
]
