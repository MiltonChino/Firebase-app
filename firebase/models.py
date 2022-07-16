
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
    
    
#     doc_ref = db.collection(u'users').document(u'aturing')
#     doc_ref.set({
#         u'first': u'Alan',
#         u'middle': u'Mathison',
#         u'last': u'Turing',
#         u'born': 1912
#         })

# users_ref = db.collection(u'users')
# docs = users_ref.stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')
# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

# doc_ref = db.collection(u'users').document(u'aturing')
# doc_ref.set({
#     u'first': u'Alan',
#     u'middle': u'Mathison',
#     u'last': u'Turing',
#     u'born': 1912
# })

# users_ref = db.collection(u'users')
# docs = users_ref.stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')

# # ADD data part 2
# data = {
#     u'name': u'Los Angeles',
#     u'state': u'CA',
#     u'country': u'USA'
# }

# # Add a new doc in collection 'cities' with ID 'LA'
# db.collection(u'cities').document(u'LA').set(data)
# # Display data
# users_ref = db.collection(u'cities')
# docs = users_ref.stream()
# print("Display new collection")
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')


# # Merge data
# city_ref = db.collection(u'cities').document(u'BJ')

# city_ref.set({
#     u'capital': True
# }, merge=True)#this statement would merge data if a BJ already exists in the collection


# # Display merge
# users_ref = db.collection(u'cities')
# docs = users_ref.stream()
# print("Display merged data of cities collection")
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')

# # END OF ADD data part 2

# # Data types
# data = {
#     u'stringExample': u'Hello, World!',
#     u'booleanExample': True,
#     u'numberExample': 3.14159265,
#     u'dateExample': datetime.datetime.now(tz=datetime.timezone.utc), #this line requeries to import datetime
#     u'arrayExample': [5, True, u'hello'],
#     u'nullExample': None,
#     u'objectExample': {
#         u'a': 5,
#         u'b': True
#     }
# }
# db.collection(u'data').document(u'one').set(data)
# # Display data collection
# users_ref = db.collection(u'data')
# docs = users_ref.stream()
# print("Display data collection to see different data types")
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')


# # Update data------------------------------
# data = {}
# # [START firestore_data_set_id_specified]
# db.collection(u'cities').document(u'new-city-id').set(data)
# # [END firestore_data_set_id_specified]
# # Display data collection
# users_ref = db.collection(u'cities')
# docs = users_ref.stream()
# print("Display a new document with new ID")
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')



# # Update timestamp
# data_ref = db.collection(u'data').document(u'one')
# data_ref.update({
#     u'dateExample': firestore.SERVER_TIMESTAMP # another way to add timestamp
# })
# # Display data collection
# users_ref = db.collection(u'data')
# docs = users_ref.stream()
# print("Display a timestamp update in one document")
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')


# # Update fields in nested objects-------------------

# # Create an initial document to update
# frank_ref = db.collection(u'users').document(u'frank')
# frank_ref.set({
#     u'name': u'Frank',
#     u'favorites': {
#         u'food': u'Pizza',
#         u'color': u'Blue',
#         u'subject': u'Recess'
#     },
#     u'age': 12
# })
# # Display data collection
# users_ref = db.collection(u'users')
# docs = users_ref.stream()
# print("Display a user with a nested collection")
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')
# # Update age and favorite color
# frank_ref.update({
#     u'age': 13,
#     u'favorites.color': u'Red'
# })
# # Display data collection
# users_ref = db.collection(u'users')
# docs = users_ref.stream()
# print("Display a user update of a nested collection")
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')
