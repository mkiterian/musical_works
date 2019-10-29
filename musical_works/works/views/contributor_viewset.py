
from musical_works.works.models import Contributor
from rest_framework import viewsets
from musical_works.works.serializers import ContributorSerializer


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer