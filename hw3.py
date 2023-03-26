import os
from google.cloud import storage
from google.cloud import pubsub_v1
from google.cloud import firestore

# Set up authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'

# Connect to Firestore
db = firestore.Client()
