from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')#route to hit
def  index(): #name of function
	return render_template('home.html')

@app.route('/about')#route hits about page
def about():
	return app.send_static_file('about.html')#returned data

@app.route('/contact')#route to hit contact page
def contact():
	return app.send_static_file('contact.html')#returned data

@app.route('/post/<postnum>')
def post1(postnum):
	return 'This is post' + postnum

@app.route('/birthday')#route to hit birthday page
def birthday():
	return 'September 22 1969'#returned information

@app.route('/greeting/<name>')#route to hit greeting page
def greeting(name):
	return 'Hello, %s!' % name #returned data

@app.route('/add/<int:a>/<int:b>')#route to hit add page
def add(a,b):
	return str(a+b)#returned information

@app.route('/multiply/<int:a>/<int:b>')#route to hit multiply page
def multiply(a,b):
	return str(a*b)#returned value

@app.route('/subtract/<int:a>/<int:b>')#route to hit subtract page
def subtract(a,b):
	return str(a-b)#returned value

@app.route('/favoritefoods')#route to hit favoritefoods page
def favoritefoods():
	favoritefoods = ["steak","pizza","bbq"]
	return jsonify(favoritefoods)#returned foods
