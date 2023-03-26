import os
import firebase_admin
from google.cloud import storage
from google.cloud import pubsub_v1
from google.cloud import firestore
from firebase_admin import credentials


# Set up authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'

# Connect to Firestore
db = firestore.Client()

# cloud Storage
storage_client = storage.Client()
bucket_name = 'bucket_name'
bucket = storage_client.get_bucket(bucket_name)

# cloud pub/sub
publisher = pubsub_v1.PublisherClient()
topic_name = 'topic_name'
topic_path = publisher.topic_path('project_id', topic_name)

# functie care posteaza un mesaj pe cloud pub/sub
def pub_info(info):
  d=info.encode('utf-8')
  publisher.publish(topic_path, d=d) 

# functie care scrie info in cloud storage
def write_data_storage(f_name,d):
  blob= bucket.blob(f_name)
  blob.upload_from_string(d)

# functie care citeste info din cloud storage
def read_data_storage(f_n):
  blob= bucket.blob(f_name)
  return blob.download_as_string()

# functie care adauga data in firestore
def add_firestore(collect, d):
  doc_id= db.collection(collect).document()
  doc_id.st(data)

#functie care preia informatie din firestore
def get_firestore_data(project_id, collection_name):
  pieces = db.collection(collection_name).get()
  res = [piece.to_dict() for piece in pieces]
  return res


pub_info('homework nr.3 Codreanu Dan 3A5')
write_data_storage('cod_sursa_hw3.txt', 'Codul temei de acasa nr.3')
# read_data_storage('exemplu5.txt')
add_firestore('exemplu_nume_colectie', {'key', 'val'})
final=get_firestore_data("exemplu_nume_proiect", "exemplu_nume_colectie")
print(final) 

