from flask import Flask, render_template, request, redirect, url_for, session, escape, send_from_directory
app = Flask(__name__)	
app.config.from_pyfile('config.py')
from views import *
if __name__=='__main__':
	app.run(debug=1)