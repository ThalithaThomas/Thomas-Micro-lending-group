import os
from flask import Flask,render_template,request,redirect,url_for

app= Flask(__name__)
app.config['ENV']= 'development'
app.config['DEBUG']= True


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contacts')
def contact():
    return render_template("contact.html")

@app.route('/personal')
def personal():
    return render_template("personal.html")


if __name__ == "__main__":
    app.run( debug=True)