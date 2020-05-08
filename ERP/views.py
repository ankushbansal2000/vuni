import pyrebase

config = {
    'apiKey': "AIzaSyBqbIlpDGidoLfL28eho8n1xN0cfbeEFr8",
    'authDomain': "vunni-b80bc.firebaseapp.com",
    'databaseURL': "https://vunni-b80bc.firebaseio.com",
    'projectId': "vunni-b80bc",
    'storageBucket': "vunni-b80bc.appspot.com",
    'messagingSenderId': "360862200900",
    'appId': "1:360862200900:web:8bbdd0fbdc9359abe13811",
    'measurementId': "G-BYDSE4ZV7Z"

}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()