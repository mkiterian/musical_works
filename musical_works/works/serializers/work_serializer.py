from musical_works.works.models import Work
from rest_framework import serializers


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    contributors = serializers.SerializerMethodField()

    def get_contributors(self, instance):
        return list(instance.contributors.values_list('name', flat=True))

    class Meta:
        model = Work
        fields = ['title', 'iswc', 'contributors']
