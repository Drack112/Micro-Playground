from django.http import JsonResponse

from .documents import *
from .serializers import *

from django_elasticsearch_dsl_drf.filter_backends import (
    CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)


def index(request):
    return JsonResponse({"status": 200})


class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentsSerializer
    lookup_field = "first_name"
    fielddata = True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]

    search_fields = (
        "title",
        "content",
    )
    multi_match_search_fields = (
        "title",
        "content",
    )
    filter_fields = {
        "title": "title",
        "content": "content",
    }
    ordering_fields = {
        "id": None,
    }
    ordering = ("id",)
