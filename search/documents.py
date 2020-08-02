from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from assignment.models import Feedback_Form

@registry.register_document
class PostDocumnet(Document):
    class Index:
        name = 'feedback'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Feedback_Form

        fields = [
            'name', 'email', 'rate', 'check', 'feed'
        ]
