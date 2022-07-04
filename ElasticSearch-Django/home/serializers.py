from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *


class NewsDocumentsSerializer(DocumentSerializer):
    class Meta:
        model = ElasticSearchDemo
        document = NewsDocument
        field = ("title", "content")

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
