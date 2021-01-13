import pymongo

from pprint import pprint
from datetime import datetime
from ids import user, passw, db

try:
    from ids import user, passw, db
except:
    user = 'stephane_isen'
    passw = 'isenBrest_29'

# Classe de la connection à la base de données
class DB():

    # Méthode pour se connecter à la bdd
    @classmethod
    def login(cls, user=user, passw=passw, db=None):
        return f"mongodb+srv://{user}:{passw}@clusterkata.b6v13.mongodb.net/{db}?retryWrites=true&w=majority"

    # Méthode pour ouvrir la connection à la bdd
    @classmethod
    def open_con(cls):
        cls.client = pymongo.MongoClient(cls.login())
        cls.db = cls.client.get_database('donations')
        cls.collection = cls.db.don

    # Méthode pour fermer la connection à la bdd
    @classmethod
    def close_con(cls):
        cls.client.close()

    # Méthode pour envoi formulaire à la bdd
    @classmethod
    def send_form(cls, name, forname, mail, donate, date=datetime.now().strftime('%d/%m/%y')):
        cls.open_con()
        cls.collection.insert_one({'name':name, 'forname':forname, 'email':mail, 'donate':donate, 'date':date})
        cls.close_con()

    # Méthode pour récupérer que le top 10 des donateurs
    @classmethod
    def get_top(cls):
        cls.open_con()
        top = list(cls.collection.find({}, {'_id':0, 'forname':1, 'name':1, 'donate':1}).sort('donate', -1))
        cls.close_con()
        return top[:12]

    # Méthode pour récupérer les donateurs tous
    @classmethod
    def get_don(cls):
        cls.open_con()
        don = list(cls.collection.find({}, {'_id':0, 'forname':1, 'name':1, 'donate':1}).sort('name', 1))
        cls.close_con()
        return don
