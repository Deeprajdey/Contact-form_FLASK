from flask import Flask,render_template,request
import csv
app = Flask(__name__)

def dtabse(data):
	field = ['name','email','message']
	with open('database.csv', mode='a') as file:
		writer = csv.DictWriter(file, delimiter=',' , fieldnames = field)
		writer.writerow(data)


@app.route('/')
def route_world():
	return render_template('index.html')

@app.route('/thank_you.html',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']
		my_dict = {'name':name,'email':email,'message':message}
		dtabse(my_dict)
		return render_template("thank_you.html",name=name)
	else:
		return render_template('index.html')

@app.route('/<username>')
def end_world(username):
	return render_template('index.html')