from flask import Flask, render_template, request, redirect, session
from decouple import config
# from models import common
import psycopg2

app = Flask(__name__)
app.config["SECRET_KEY"] = "My secret key"


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route("/login", methods=["POST"])
def login_form():
  email = request.form.get("email")
  password = request.form.get("password")
  if email == "example@example.com" and password == "password123":
        session['logged_in'] = True
        return redirect('/gallery')
  else:
        return render_template('login.html', error_message="Invalid email or password")



@app.route('/signup')
def sign_up():
    return render_template('sign_up.html')


@app.route('/gallery')
def gallery():
    connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items")
    results = cursor.fetchall()
    print(results)  
    connection.commit()    
    return render_template('gallery.html', items=results)


@app.route('/cart')
def shopping_cart():
    return render_template('shopping_cart.html')


if __name__ == "__main__":
    app.run(debug=True)
