from db import DB
from datetime import datetime
from random import randrange, choice

forname_li = ['Liam', 'Noah', 'Oliver', 'William', 'Elijah', 'James', 'Benjamin', 'Lucas', 'Mason', 'Ethan', 'Olivia', 'Emma',
         'Ava', 'Sophia', 'Isabella', 'Charlotte', 'Amelia', 'Mia', 'Harper', 'Evelyn', 'Abbey', 'Addison', 'Adal', 'Alex',
          'Ali', 'Thomas', 'Camille', 'Pereg', 'Baptiste', 'Jérémy', 'César', 'Paul', 'Pauline', 'Eva', 'Christelle', 'Patricia',
          'Julien', 'Céline', 'Gwendolyne', 'Coralie', 'Stéphanie', 'Brigitte', 'Laura', 'Clémentine', 'Clara', 'Capucine',
          'Morgane', 'Jason', 'Kevin', 'Bob', 'Théo', 'Léopold', 'Reagan', 'Maud', 'Julie', 'David', 'Hermione', 'Cheryl', 'Cassandra',
          'Christopher', 'Christophe', 'Peter', 'Billy', 'Joan', 'Joe', 'John', 'Lyn', 'Dirk', 'Don', 'Ben', 'Jim', 'Christian', 'Assa',
          'Fatou', 'Nelson', 'Talia', 'Bruce', 'Micheline', 'Ana', 'Sean', 'Victoria']
name_li = ['Bokalli', 'Bonneau', 'Chaigneau', 'Cloatre', 'Furiga', 'Guillen', 'Hergoualc\'h', 'Ibanni', 'Karfaoui', 'LeBerre',
        'LeGoff', 'LeJoncour', 'LeMoal', 'Maintier', 'Moulard', 'Petron', 'Rioual', 'Sabia', 'Verpoest', 'Anderson', 'Dupuis', 'Dupont',
        'Fields', 'Morris', 'Landers', 'Flanders', 'Simpson', 'Swift', 'Derulo', 'Derm', 'Xin', 'Salvia', 'Davis', 'Glenn', 'Neill', 'Ameche',
        'Mandella', 'Bogarde', 'Berry', 'MacLaine', 'Neil', 'Owen', 'Spector', 'Dalton', 'Fournirer', 'Louis', 'Dennis', 'Fitzalan', 'Jenner',
        'Elbe', 'Smith', 'Todd', 'Bisset', 'Cruise', 'Glaser', 'Charles', 'Fontaine', 'Barrymore', 'Laden', 'Traoré', 'Polina']

for i in range(100):
    name = choice(name_li)
    forname = choice(forname_li)
    email = f'{name.lower()}.{forname.lower()}@gmail.com'
    donate = randrange(500)
    date = f'20/{randrange(1, 12)}/{randrange(1, 30)}'
    if len(date.split('/')[1]) < 2:
        date = date[:3] + '0' + date[3:]
    if len(date.split('/')[2]) < 2:
        date = date[:6] + '0' + date[6:]
    DB.send_form(name, forname, email, donate, date)
    print(date)
