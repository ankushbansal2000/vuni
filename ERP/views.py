import pyrebase

config = {
    'apiKey': "AIzaSyCm5BzstqFAR5J1fh9RK5kPQR4sslkVHcw",
    'authDomain': "vunni-24de6.firebaseapp.com",
    'databaseURL': "https://vunni-24de6.firebaseio.com",
    'projectId': "vunni-24de6",
    'storageBucket': "vunni-24de6.appspot.com",
    'messagingSenderId': "83041827292",
    'appId': "1:83041827292:web:0d85c8b283d18649c47719",
    'measurementId': "G-Y4BQCQD9RM"

}
firebase = pyrebase.initialize_app(config)
database = firebase.database()
storage = firebase.storage()