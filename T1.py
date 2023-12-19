from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/mobile_store'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('index.html', products=products)

# Add other routes for handling user actions (e.g., add to cart, purchase)

if __name__ == '__main__':
    app.run(debug=True)