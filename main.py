from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/publications', methods=['GET'])
def publications():
    return render_template("publications.html")

@app.route('/blog', methods=['GET'])
def blog():
    return render_template("blog.html")
