from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Initialisation de la base de données'
    
    def handle(self, *args, **options):
        filePath = 'api/data'
        chichieractual = __file__
        chemiseabsolute = os.path.abspath(chichieractual)

        print("Vous êtes dans le fichier :", chemiseabsolute)
        return None
