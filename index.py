import firebase_admin
from firebase_admin import firestore, credentials

#recupero credenziali
cred = credentials.Certificate("test-17a52-firebase-adminsdk-35dnx-f46f4f690a.json")
#inizializzamo l'app
app = firebase_admin.initialize_app(cred)

# Application Default credentials are automatically created.
db = firestore.client()

users_ref = db.collection('user') #"user" nome db
docs = users_ref.stream()

#alovelace è un id casuale
doc_ref = db.collection('user').document('alovelace')
doc_ref.set({
    'nome': 'Ada',
    'cognome': 'Lovelace',
    'nascita': 1815
})

for doc in docs:
    print(doc.to_dict()['nome'])
    #print(f'{doc.id} => {doc.to_dict()}')
print('---------')


cities_ref = db.collection("user")
query = cities_ref.order_by("nome").limit(2) # gli ordina per nome (con 
                                             #precedenza alle maiuscole) e 
                                             #con limit settiamo quanti record
                                             #recuperare
#limit_to_last(2) prende gli ultimi 2 e gli ordina al contrario
results = query.get()

for doc in results:
    print(doc.to_dict()['nome'])
print('---------')

user_ref = db.collection('user')
query = user_ref.where('nome', '==', "patch")
results = query.get()


for doc in results:
    print(doc.to_dict()['nome'])