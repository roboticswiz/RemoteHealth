import pyrebase

#variable setup

config = {
  "apiKey": "AIzaSyCCJ8mPbuKJb-Hv-ABgD1DnSkaEQdTgprk",
  "authDomain": "remotehealth-40d3f.firebaseapp.com",
  "projectId": "remotehealth-40d3f",
  "storageBucket": "remotehealth-40d3f.appspot.com",
  "serviceAccount": "servicekey.json",
  "databaseURL": " "
 # "messagingSenderId": "1078999652192",
 # "appId": "1:1078999652192:web:55e96bb3b0da32f2f17005",
  #"measurementId": "G-V114G87MVC",
}

firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()


storage.child ("auscultation/bot.JPEG").put("botjpeg.JPEG")