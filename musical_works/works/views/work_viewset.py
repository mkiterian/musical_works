from musical_works.works.models import Work
from rest_framework import viewsets
from musical_works.works.serializers import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

