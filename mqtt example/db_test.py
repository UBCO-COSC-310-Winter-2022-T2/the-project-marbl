import firebase_admin
import time

cred_obj = firebase_admin.credentials.Certificate('./cosc310-marbl-firebase-adminsdk-8ced8-4927d63ad0.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://cosc310-marbl-default-rtdb.firebaseio.com/'
	})

from firebase_admin import db

#dbref = db.reference("/")

dbref = db.reference("/Messages/")

#save message
dbref.push().set({ 
    "author": "guy 1",
  	"time": time.time(), # in seconds (with fractions)
  	"msg": "wow again! ",
})

#get all messages after time 1680202348.6992225 (approx 2 microsec past the first four messages, 1 microsec didn't work for some reason) sorted by time
print(dbref.order_by_child("time").start_at(1680202348.6992225).get())
