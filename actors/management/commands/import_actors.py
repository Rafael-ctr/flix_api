import csv
from django.core.management.base import BaseCommand
from actors.models import Actor
from datetime import datetime


class Command (BaseCommand):
    help = "comando para importar lista de atores"

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='nome do arquivo CSV na raiz do projeto'
        )

    def handle(self, *arg, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'].strip(), '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(name=name, birthday=birthday, nationality=nationality)

            self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO'))

        

        

