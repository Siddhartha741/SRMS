from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'seetharama_secret_key'

# In-memory storage for demonstration
users = {'admin@example.com': 'admin123'}
products = [
    {'id': 1, 'name': 'Paracetamol', 'price': 20, 'stock': 100},
    {'id': 2, 'name': 'Surgical Gloves', 'price': 150, 'stock': 200},
    {'id': 3, 'name': 'Thermometer', 'price': 250, 'stock': 50},
]
orders = []
cart_items = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            session['user'] = email
            return redirect(url_for('products_page'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users:
            return 'User already exists'
        users[email] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/products')
def products_page():
    query = request.args.get('search', '')
    filtered = [p for p in products if query.lower() in p['name'].lower()]
    return render_template('products.html', products=filtered, search=query)

@app.route('/add_to_cart/<int:pid>')
def add_to_cart(pid):
    for product in products:
        if product['id'] == pid and product['stock'] > 0:
            cart_items.append(product)
            product['stock'] -= 1
            break
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    return render_template('cart.html', cart_items=cart_items)

@app.route('/checkout')
def checkout():
    if cart_items:
        orders.append({'user': session.get('user', 'guest'), 'items': list(cart_items)})
        cart_items.clear()
    return redirect(url_for('order_history'))

@app.route('/order-history')
def order_history():
    user_orders = [o for o in orders if o['user'] == session.get('user', 'guest')]
    return render_template('order_history.html', orders=user_orders)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', products=products, users=list(users.keys()), orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
