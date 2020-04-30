from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.fields import IntegerField

class ReusableForm(Form):
    name = TextField('Nome', validators=[validators.required()])
    email = EmailField('Email address', validators=[validators.required()])
    mobile_phone = IntegerField('Telefone', validators=[validators.required()])
    mensagem = TextAreaField('Mensagem', validators=[validators.required()])