from flask import Flask, render_template, request,redirect,url_for
import csv
app = Flask(__name__)
import pandas


@app.route ('/')
def home1 ():
	return render_template ('contact.html')

@app.route ('/register')
def register ():
	return render_template ('contact.html')

@app.route ('/display')
def display ():
	file = pandas.read_csv("contactdb.csv")
	file.to_html('templates/information.html')
	return render_template ('information.html')

@app.route ('/loginsus')
def loginsus ():
	return render_template("info.html")

@app.route('/loginenter', methods=['POST', 'GET'])
def loginenter():
	database = open("database.csv","r")
	if request.method == 'POST':
		data = request.form.to_dict()
		emailid = data["emailid"]
		epassword = data["epassword"]
		csv_reader = csv.reader(database)
		allrow = []
		for row in csv_reader:
			if row[0]==emailid and row[1]==epassword:
				m = 100
				break
		if m==100:
			return redirect(url_for("loginsus"))
		else:
			return "check password and try again"


@app.route('/login' ,methods=['POST','GET'])
def login():
	return render_template('login.html')

def write_to_csv (data):
	with open('database.csv', mode = 'a',newline="") as database:
		emailid = data["emailid"]
		epassword = data["epassword"]
		scretekey = data["scretekey"]
		csv_writer = csv.writer(database, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([emailid, epassword, scretekey])

@app.route('/successnew', methods= ['POST','GET'])
def success():
	return render_template("successnew.html")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect(url_for("success"))
	else:
		return 'Some thing went wrong ... Try again'

def write_to_csv_contact(data):
	with open('contactdb.csv', mode = 'a',newline="") as database:
		name = data["name"]
		phone = data["phone"]
		emailid = data["emailid"]
		csv_writer = csv.writer(database, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([name, phone, emailid])

@app.route('/contact_enter', methods=['POST', 'GET'])
def contact_enter():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv_contact(data)
		return "success"
	else:
		return 'Some thing went wrong ... Try again'
    

if __name__ == '__main__':
	app.run (debug = True)