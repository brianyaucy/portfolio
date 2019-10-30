from flask import Flask, render_template, url_for, request, redirect
import csv
import sys


app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/works")
def works():
    return render_template('works.html')

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/components")
def components():
    return render_template("components.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

@app.route("/favicon.ico")
def icon():
    return render_template("static/assets/favicon.ico")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return 'did not save to database ...'
    else:
        return 'Error!'


def write_to_csv(data):
    with open('database.csv', 'a', newline="") as database:
        email, subject, message = data['email'], data['subject'], data['message']
        csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow((email,subject,message))
