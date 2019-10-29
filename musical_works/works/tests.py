from django.test import TestCase

# Create your tests here.
from io import StringIO
from django.core.management import call_command
from django.test import TestCase

class LoadDataTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command(
            'ingest_data_from_file', 'test_works_metadata.csv', stdout=out)
        self.assertIn('created successfully', out.getvalue())