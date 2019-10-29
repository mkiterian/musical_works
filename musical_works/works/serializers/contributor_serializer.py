from musical_works.works.models import Contributor
from rest_framework import serializers


class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    works_list = serializers.SerializerMethodField()

    def get_works_list(self, instance):
        return list(instance.works_list.values_list('title', flat=True))

    class Meta:
        model = Contributor
        fields = ['name', 'works_list']
