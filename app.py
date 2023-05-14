from flask import Flask, render_template, request, redirect, session
from decouple import config
import psycopg2
import os

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

    # connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))

    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
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

        # connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))

        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
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

    # connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))

    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items")
    results = cursor.fetchall()
    connection.commit()  
    cursor.close()
    connection.close()
    return render_template('gallery.html', items=results)


@app.route('/cart')
def shopping_cart():

    # connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))

    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute("SELECT items.item_name, items.price, shopping_cart.quantity, items.id FROM shopping_cart JOIN items ON shopping_cart.item_id=items.id")
    items = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return render_template('shopping_cart.html', items=items)


@app.route('/cart', methods=['POST'])
def add_to_cart():
    item_id = request.form['item_id']
    quantity = request.form['quantity']

    # connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))

    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    # check if the item already exists in the shopping cart
    cursor.execute("SELECT * FROM shopping_cart WHERE item_id = %s", (item_id,))
    result = cursor.fetchone()
    if result:
        # update its quantity if the item exists
        new_quantity = result[2] + int(quantity)
        cursor.execute("UPDATE shopping_cart SET quantity = %s WHERE item_id = %s", (new_quantity, item_id))
    else:
        # insertnew item with the quantity
        cursor.execute("INSERT INTO shopping_cart (item_id, quantity) VALUES (%s, %s)", (item_id, quantity))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/cart')



@app.route('/remove_item', methods=['POST'])
def remove_item():
    item_id = request.form['item_id'] 
    print(item_id)
    if item_id:
        print(item_id)
        item_id = int(item_id)

        # connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))

        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute("DELETE FROM shopping_cart WHERE item_id = %s", (item_id,))
        connection.commit()
        cursor.close()
        connection.close()
    return redirect('/cart')


if __name__ == "__main__":
    app.run(debug=True)
