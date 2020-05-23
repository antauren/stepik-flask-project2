from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import TelField
from wtforms.validators import InputRequired


class ClientForm(FlaskForm):
    name = StringField('Вас зовут', [InputRequired(message='Это поле не может быть пустым.')])
    phone = TelField('Ваш телефон', [InputRequired(message='Это поле не может быть пустым.')])
    submit = SubmitField()
