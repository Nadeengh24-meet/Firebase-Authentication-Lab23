from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try: 
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            error = 'Authentication failed'
    return render_template("signup.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


@app.route("/signin", methods= ['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try: 
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            error = 'Authentication failed'
    return render_template("signin.html")


    
Config = {

  "apiKey": "AIzaSyChVjCGltcEOF3rDZe12kEnHqBEdBhO388",
  "authDomain": "nadeen-79c65.firebaseapp.com",
  "projectId": "nadeen-79c65",
  "storageBucket": "nadeen-79c65.appspot.com",
  "messagingSenderId": "15669696773",
  "appId": "1:15669696773:web:b1e34f1fccd4d9b865bf6c",
  "measurementId": "G-L9PB2L26XY", 
  "databaseURL": ""

}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

if __name__ == '__main__':
    app.run(debug=True)