from flask import Flask, render_template, request, redirect, session
from decouple import config
# from models import common
import psycopg2

app = Flask(__name__)
app.config["SECRET_KEY"] = "My secret key"


@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')


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

    connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()

    # if user exists, log them in and redirect to gallery
    if user:
        session['logged_in'] = True
        return redirect('/gallery')
    # if user does not exist, display error message
    else:
        return render_template('login.html', error_message="Invalid email or password")




@app.route('/signup', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        mobile = request.form.get("mobile")
        email = request.form.get("email")
        password = request.form.get("password")
        
        connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (full_name, mobile, email, password) VALUES (%s, %s, %s, %s)", (full_name, mobile, email, password))
        connection.commit()
        cursor.close()
        connection.close()
        session['logged_in'] = True
        return redirect('/gallery')
    else:
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

@app.route('/cart', methods=['POST'])
def add_to_cart():
    item_name = request.form['item_name']
    quantity = request.form['quantity']
    connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO shopping_cart (item_name, quantity) VALUES (%s, %s)", (item_name, quantity))
    connection.commit()
    cursor.close()
    connection.close()
    
    return render_template('shopping_cart.html')



if __name__ == "__main__":
    app.run(debug=True)
