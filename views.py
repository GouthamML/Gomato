import os
from app import app
from app import *
from flask_mysqldb import MySQL
from werkzeug import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from restaurant import *

app.config['SECRET_KEY']='hard to guess string'

app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'gomato'

mysql=MySQL(app)

class NameForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('email')
    password = PasswordField('passowrd')
    submit = SubmitField('Submit')
    name = StringField('NAME')
    Address = StringField('ADDRESS')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form=NameForm()
    return render_template('signup.html', form=form)

@app.route('/register', methods=['POST'])
def register():
	form = NameForm()
	username = form.username.data
	password = form.password.data
	cur=mysql.connection.cursor()
	print username, password
	cur.execute("insert into login(username, password) values (%s, %s)",(username, password))
	mysql.connection.commit()
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	form=NameForm()
	return render_template('login.html', form = form)

@app.route('/check', methods=["POST"])
def check():
    form=NameForm()
    cur=mysql.connection.cursor()
    if request.method == 'POST':
        username_form  = form.username.data
        cur.execute("SELECT username AS uname FROM login WHERE username = '" + username_form +"'")
        fetched_name = cur.fetchone()
        if fetched_name == None:
            return 'Invalid username'
            
            
        password_form  = form.password.data
        cur.execute("SELECT password AS pword FROM login WHERE username = '"+ username_form +"'")
        print username_form, password_form, fetched_name
            
        for row in cur.fetchall():
            if password_form == row[0]:
                print cur.fetchall()
                session['username'] = form.username.data
                return redirect(url_for('index'))
            return 'Invalid password'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/')
def index():

	form=NameForm()
    	cur=mysql.connection.cursor()
    	if 'username' in session:
        	username_session = session['username']
        	return render_template('index.html',name = username_session, form = form)
    	return redirect(url_for('login'))

@app.route('/details', methods= ['GET','POST'])
def details():
	r_name = []
	r_address = []
	r_lat = []
	r_lan = [] 
	form = NameForm()
	inputstring = form.name.data
	mealtype = request.form['food']
	result = findARestaurant(mealtype, inputstring)
	print result['response']['venues'][0]['location']['formattedAddress']
	for i in range(1,10):
		r_name.append(result['response']['venues'][i]['name'])
		r_address.append(result['response']['venues'][i]['location']['formattedAddress'])
		r_lat.append(result['response']['venues'][i]['location']['lat'])
		r_lan.append(result['response']['venues'][i]['location']['lng'])
	print r_name
	print r_address
	
	return render_template('details.html', info = zip(r_name,r_address,r_lan,r_lat))
	# print result['response']['venues'][1]['location']['address']




