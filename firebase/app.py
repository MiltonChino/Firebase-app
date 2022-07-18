# Create a simple app to keep track of my tasks and
from posixpath import relpath
import os
from queue import Empty
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))
path = relpath('fib-pydj-test-mc-firebase-adminsdk-ioidp-59748da794.json')
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)

# from google.cloud import firestore

class Task(object):
    def __init__(self, title, desc, time, label,label_exists=True):
        self.title = title
        self.desc = desc
        self.time = time
        self.label = label
        self.label_exists = label_exists

    # def displayFields(self):
    #     print (f'Title: {self.title}')
    #     print (f'Description: {self.desc}')
    #     print (f'Time: {self.time}')
    #     print (f'Label: {self.label}')

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        task = Task(source[u'Title'], source[u'Description'], source[u'Time'], source[u'Label'])

        if u'Label' in source:
            task.label = source[u'Label']


        return task
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'Title': self.title,
            u'Description': self.desc,
            u'Time': self.time
        }

        if self.label:
            dest[u'Label'] = self.label

        return dest
        # [END_EXCLUDE]


    def __repr__(self):
        return(
            f'Task(\
                title={self.title}, \
                description={self.desc}, \
                time={self.time}, \
                label={self.label}\
            )'
        )



def PrintMenu():
    print("________________________")
    print("Please enter one option:")
    print("1. Display Tasks")
    print("2. Add New Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("0. Quit App")
    print("________________________")
    

def main():
    start_app = True
    while start_app:
        option = ''
        PrintMenu()
        # database = quickstart_new_instance()
        option = input("Enter option: ")
        if option == "1":
            displayAllTasks()
        if option == "2":
            addTask()
        if option == "3":
            tasks = getTasks()
            task_id = input("Task ID: ")
            if task_id in tasks.id:
                editTask()
        if option == "4":
            deleteTask()
        if option == '0':
            start_app = False
    
    print ('Thank You!')


def displayAllTasks():
    db = firestore.client()
    users_ref = db.collection(u'tasks')
    docs = users_ref.stream()
    print ('=======================')
    print("Display Tasks List")
    print("__________________")
    for doc in docs:
        displayFields(doc.to_dict())
        print("-----------------")
        # print(f'{doc.id} => {doc.to_dict()}') #No need of this line
    print('========================')

def addTask():
    # from google.cloud import firestore

    db = firestore.client()
    tasks = db.collection(u'tasks').document()
    label_exists = True   
    # Ask for values
    print('====================================')
    print('Please enter the following values: ')
    title = input(f'Title of the task: ')
    desc = input(f'Description of the task: ')
    time = input(f'Due date: ')
    label = input(f'Label of the task (if there is no label, press enter): ')
    if label == '':
        label_exists = False

    task = Task(title,desc,time,label,label_exists)
    tasks.set(task.to_dict())

    print('-------------------')
    print('Task submitted: ')
    displayFields(task.to_dict())
    print('====================================')

def displayTask():
    db = firestore.client()
    tasks_ref = db.collection(u'tasks').where(u'Label', u'==', u'BYUI' )
    query = tasks_ref.stream()
    n_tasks = 0
    print('================')
    print("Display Task")
    for task in query:
        # print(f'{task.id} => ')
        displayFields(task.to_dict())
        print()
        n_tasks+=1
    print('_______________________')
    print(f'Tasks found: {n_tasks}')
    print('=======================')

def displayFields(tasks):
    title = tasks['Title']
    desc = tasks['Description']
    time = tasks['Time']
    label = tasks['Label']

    print(f'Title: {title}')
    print(f'Description: {desc}')
    print(f'Time: {time}')
    if label != Empty:
        print(f'Label: {label}')

def taskProperties():
    db = firestore.client()
    doc_ref = db.collection(u'tasks')

    doc_ref.set({
        u'Title': u'Add your title',
        u'Time': u'Add your end time ',
        u'Description': u'Add your description',
        u'Tag': "Add your tag"
        })

    print("")

def getTasks():
    db = firestore.client()
    task_ref = db.collection(u'tasks')
    tasks = task_ref.stream()
    pass


def editTask():
    db = firestore.client()
    users_ref = db.collection(u'tasks')
    docs = users_ref.stream()
    pass

def deleteField():
    db = firestore.client()
    city_ref = db.collection(u'cities').document(u'BJ')
    city_ref.update({
        u'capital': firestore.DELETE_FIELD
    })

def deleteTask():
    db = firestore.client()
    tasks_ref = db.collection(u'tasks').where(u'id', u'==', u'0' )
    query = tasks_ref.stream()
    for task in query:
        if task.exists:
            task.delete()
            print('Task deleted')

    # docs = db.collection(u'tasks')

    # # for task in docs:
    # if docs.exists:
    #     print(f'Document data: {docs.to_dict()}')
    #     confirmation = input('delete task (y/n)?:')
    #     if confirmation == 'y':
    #         docs.delete()
    #         print(f'Task deleted')
    #     else:
    #         print(f'OK')

    # else:
    #     print(u'No such document!')
    
    # print ('=======================')


if __name__ == "__main__":
    main()