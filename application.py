from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for

import datetime
import os


app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.before_request
def before_request():
	pass


# HOME


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/layout/")
def layout():
	return render_template("layout.html")



# SERVICES


@app.route("/digital_forensics/")
def digital_forensics():
	return render_template("digital_forensics.html")

@app.route("/e_discovery/")
def e_discovery():
	return render_template("e_discovery.html")

@app.route("/cyber_security/")
def cyber_security():
	return render_template("cyber_security.html")



# COMPANY

@app.route("/about_us/")
def about_us():
	return render_template("about_us.html")



# CONTACT

@app.route("/contact/")
def contact():
	return render_template("contact.html")


# LEGAL NOTICE

@app.route("/disclaimer/")
def disclaimer():
	return render_template("disclaimer.html")


#  404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page-404.html'), 404




if __name__ == "__main__":
	app.run()
