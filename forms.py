from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField,BooleanField,IntegerField,PasswordField,StringField,DecimalField
from wtforms.fields import DateField
from wtforms.validators import InputRequired, NumberRange, EqualTo
from decimal import ROUND_HALF_UP

class RegistrationForm(FlaskForm):
    user_id = StringField("Userid:",
                          validators = [InputRequired()])
    password =PasswordField("password:",
                            validators = [InputRequired()])
    password2 = PasswordField("Re-enter the password:",
                    validators=[InputRequired(),EqualTo("password")])
    submit = SubmitField("submit")

class LoginForm(FlaskForm):
    user_id = StringField("user_id",
                          validators = [InputRequired()])
    password = PasswordField("password:",
                             validators = [InputRequired()])
    submit = SubmitField("submit")



class allergiesForm(FlaskForm):
    dairy = BooleanField("if you are alergic to dairy tick the box:")
    soy = BooleanField("if you are alergic to soy tick the box:")
    eggs = BooleanField("if you are alergic to eggs tick the box :")
    wheat = BooleanField("if you are alergic to wheat tick the box:")
    nuts = BooleanField("if you are alergic to tree nuts tick the box:")
    fish = BooleanField("if you are alergic to fish tick the box:")
    chicken =  BooleanField("if you are alergic to chicken tick the box:")
    
    submit = SubmitField("submit")
