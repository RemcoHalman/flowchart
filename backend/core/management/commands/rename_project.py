import os
from django.core.management.base import BaseCommand

current_project_name = os.environ.get("DJANGO_SETTINGS_MODULE").split('.')[0]

class Command(BaseCommand):
    help = 'Renames your Django project to your Project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django project name')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # Bit of logic to rename the project
        files_to_rename = [
             f'{current_project_name}/settings.py',
             f'{current_project_name}/wsgi.py',
             'manage.py',
             'Procfile',

        ]
        folder_to_rename = f'{current_project_name}'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(folder_to_rename, new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('The project has been renamed to %s' % new_project_name))
        self.stdout.write(self.style.WARNING(f'Dont forget to capitalize all {new_project_name} tags in the html templates'))
