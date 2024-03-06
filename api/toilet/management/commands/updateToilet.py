from django.core.management.base import BaseCommand
import os
import json
from toilet.models import Toilet

class Command(BaseCommand):
    help = 'Initialisation de la base de données'
    
    def handle(self, *args, **options):
        chemiseabsolute = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'data')
        
        cmptAdded = 0
        cmptTotal = 0
        cmptError = 0

        
        for file in os.listdir(chemiseabsolute):
            if not '.json' in file: continue

            currentData = None
            
            with open(os.path.join(chemiseabsolute, file), 'r') as f:
                currentData = json.load(f)

            for toilet in currentData:
                cmptTotal += 1
                
                try:
                    keyId = 'id' if 'id' in toilet else 'edit_id'

                    Toilet.objects.create(
                        toiletId=toilet[keyId],
                        toiletLatitude=toilet['latitude'],
                        toiletLongitude=toilet['longitude'],
                        toiletName=toilet['name'],
                        toiletStreet=toilet['street'],
                        toiletCity=toilet['city'],
                        toiletCountry=toilet['country'],
                        toiletDirection=toilet['directions'],
                        toiletUpVote=toilet['upvote'],
                        toiletDownVote=toilet['downvote']
                    )
                
                    cmptAdded += 1
                except Exception as e:
                    cmptError += 1
                    self.stdout.write(self.style.ERROR(f'Error toilette {cmptTotal} (err {cmptError}) | ({str(e)})'))


        self.stdout.write(self.style.SUCCESS(f'Vous avez ajouté {cmptAdded} toilettes sur {cmptTotal} données'))
        return None
