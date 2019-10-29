import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from musical_works.works.models import Work, Contributor
from musical_works.settings import BASE_DIR


class Command(BaseCommand):
    help = "Ingest works data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", help="Name of csv file with works data")

    def _ingest_data_from_file(self, file_name):
        file_path = os.path.join(BASE_DIR, "resources", "csv", file_name)

        with open(file_path, encoding="utf-8") as data_file:
            next(data_file)
            data = csv.reader(data_file)
            for row in data:
                title = row[0]
                contributor_names = row[1].split("|")
                iswc = row[2]

                try:
                    works = Work.objects.filter(
                        Q(iswc=iswc)
                        | Q(Q(title=title), Q(contributors__name__in=contributor_names))
                    )
                    work = None

                    if works.exists():
                        work = works.first()
                        self._update_iswc(works, iswc)
                    else:
                        work = Work.objects.create(title=title, iswc=iswc,)
                        self.stdout.write(
                            "\nWork titled {} created successfully".format(work.title)
                        )

                    self._update_contributors(work, contributor_names)
                except Exception as e:
                    raise CommandError(str(e))

    def _update_contributors(self, work, contributor_names):
        for name in contributor_names:
            contributor, _ = Contributor.objects.get_or_create(name=name)
            if not work.contributors.all().filter(id=contributor.id).exists():
                work.contributors.add(contributor)

    def _update_iswc(self, work_queryset, iswc):
        work = work_queryset.first()
        if not work.iswc and iswc:
            work_queryset.update(iswc=iswc)
            self.stdout.write(
                "\nWork titled {} iswc updated to {}".format(work.title, iswc)
            )

    def handle(self, *args, **options):
        works_file = options["csv_file"]
        self._ingest_data_from_file(works_file)
