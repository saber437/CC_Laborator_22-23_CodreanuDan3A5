import os
from google.cloud import storage
from google.cloud import pubsub_v1
from google.cloud import firestore

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

def pub_info(info):
  d=info.encode('utf-8')
  publisher.publish(topic_path, d=d) 

def write_data(f_name,d):
  blob= bucket.blob(f_name)
  blob.upload_from_string(d)
  
def read_data(f_n):
  blob= bucket.blob(f_name)
  return blob.download_as_string()

def add_firestore(collect, d):
  doc_id= db.collection(collect).document()
  doc_id.st(data)



