from musical_works.works.models import Work
from rest_framework import viewsets
from musical_works.works.serializers import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    serializer_class = WorkSerializer

    def get_queryset(self):
        queryset = Work.objects.all()
        iswc = self.request.query_params.get('iswc', None)
        if iswc is not None:
            queryset = queryset.filter(iswc=iswc)
        return queryset

