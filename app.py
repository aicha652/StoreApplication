#!/usr/bin/python3
from flask import Flask, render_template
from flask import Flask
from models import *

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def products_list():
    """display a HTML page with the states listed in alphabetical order"""
    products = storage.all("Product").values()
    return render_template('products_list.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)