from posixpath import relpath
# Create your models here.
import os
relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))
# Working with Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Use a service account
path = relpath("fib-pydj-test-mc-firebase-adminsdk-ioidp-59748da794.json")
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
        u'first': u'Alan',
        u'middle': u'Mathison',
        u'last': u'Turing',
        u'born': 1912
    })

users_ref = db.collection(u'users')
docs = users_ref.stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')