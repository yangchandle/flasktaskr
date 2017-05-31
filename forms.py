# FlaskTaskr/forms.py


from flask_wtf import Form 
from wtforms import StringField, DateField, IntegerField,\
	SelectField, PasswordField
from wtforms.validators import DataRequired, length, EqualTo, Email


class AddTaskForm(Form):
	task_id = IntegerField()
	name = StringField('Task Name', validators=[DataRequired()])
	due_date = DateField(
		'Date Due (mm/dd/yyyy)',
		validators=[DataRequired()], format='%m/%d/%Y'
	)
	priority = SelectField(
		'Priority',
		validators=[DataRequired()],
		choices=[
			('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
			('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
		]
	)
	status = IntegerField('Status')


class RegisterForm(Form):
	name = StringField(
		'Username',
		validators=[DataRequired(), length(min=6, max=25)]
	)
	email = StringField(
		'Email',
		validators=[DataRequired(), length(min=6, max=40)]
	)
	password = PasswordField(
		'password',
		validators=[DataRequired(), length(min=6, max=40)]
	)
	confirm = PasswordField(
		'Repeat Password',
		validators=[DataRequired(), EqualTo('password')]
	)



class LoginForm(Form):
	name = StringField(
		'username',
		validators=[DataRequired()]
	)
	password = PasswordField(
		'password',
		validators=[DataRequired()]
	)