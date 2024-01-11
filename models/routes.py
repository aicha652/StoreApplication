from flask import Flask, render_template, session, request, redirect, url_for, flash
from .forms import LoginForm
from models import User, bcrypt
from models.products import Product
from models import storage

app = Flask(__name__)

@app.route("/admin")
def admin():
    if "email" not in session:
        flash(f"Please Log In", "danger")
        return redirect(url_for("login"))
    products = storage.all(Product).values()
    return render_template("admin/index.html", title="Admin Page", products=products)