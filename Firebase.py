import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

class Firebase:
    def __init__(self):
        self._serviceAccount = credentials.Certificate('ecologic-center-firebase-adminsdk-9ip96-d8a8858aa7.json')
        firebase_admin.initialize_app (self._serviceAccount, {
            'databaseURL': 'https://ecologic-center.firebaseio.com'
            })
        self._db = db.reference()

    def insertaBomba(self, segundos, fecha):
        doc = {
            'fecha' : fecha, 
            'segundos': segundos
            }
            
        pushDoc = self._db.child('Bomba').push(doc)
        id = pushDoc.key
        print('Documento insertado en Firebase id = {}'.format(id))

    def insertaSensores(self, temperatura, humedad, ldr, humedadPlanta, fecha):
        doc = {
            'fecha' : fecha, 
            'temperatura' : temperatura,
            'humedad' : humedad,
            'humedadPlanta': humedadPlanta,
            'ldr': ldr
            }
            
        pushDoc = self._db.child('Sensores').push(doc)
        id = pushDoc.key
        print('Documento insertado en Firebase id = {}'.format(id))
