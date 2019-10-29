from io import StringIO
from collections import OrderedDict

from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command
from django.test import TestCase
from rest_framework.test import APIClient

from musical_works.works.models import Contributor, Work
from musical_works.works.serializers import WorkSerializer


class IngestDataFromFileTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command(
            'ingest_data_from_file', 'test_works_metadata.csv', stdout=out)
        self.assertIn(
            'Work titled Test Work created successfully', out.getvalue())
        self.assertTrue(Contributor.objects.filter(name="Jane Doe").exists())
        contributors = Work.objects.filter(
            iswc="T9123456789").values_list("contributors__name", flat=True)
        self.assertTrue("Marshall Mathers" in contributors)


class WorkViewSetTestCase(TestCase):
    client = APIClient()

    def setUp(self):
        self._create_test_work(
            title="Nonstop", iswc="T123456780", name="Aubrey Drake Graham")
        self._create_test_work(
            title="Ken Lee", iswc="T123456781", name="Natasha")

    def test_get_all_works(self):
        response = self.client.get("/works/")
        expected = Work.objects.all()
        serialized = WorkSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)

    def test_get_works_filtered_by_iswc(self):
        iswc = "T123456781"
        req_params = {"iswc": iswc}
        response = self.client.get("/works/", data=req_params)
        expected = Work.objects.get(iswc=iswc)
        serialized = WorkSerializer(expected)
        self.assertEqual(response.data, [OrderedDict(serialized.data)])

    def _create_test_work(self, title, iswc, name):
        work = Work.objects.create(title=title, iswc=iswc)
        contributor = Contributor.objects.create(name=name)
        work.contributors.add(contributor)
