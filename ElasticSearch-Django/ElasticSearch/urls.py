from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home.views import *

urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("search/", PublisherDocumentView.as_view({"get": "list"})),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
