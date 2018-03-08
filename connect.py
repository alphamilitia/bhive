import pyrebase
from flask import render_template

config = config = {
    'apiKey': "AIzaSyBarjxK5kmEF7tnZIO9tpIF4t9FzBnsfjk",
    'authDomain': "bhive-5f732.firebaseapp.com",
    'databaseURL': "https://bhive-5f732.firebaseio.com",
    'projectId': "bhive-5f732",
    'storageBucket': "bhive-5f732.appspot.com",
    'messagingSenderId': "377032490280"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


def signin(request):
    return render_template(request.method, "login.html")


def postsign(request):
    return render_template(request.method, "user.html")
