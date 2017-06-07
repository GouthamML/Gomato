import os
from app import app
from app import *
from flask_mysqldb import MySQL
from werkzeug import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

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
    Name = StringField('NAME')
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
	return "Done!"



