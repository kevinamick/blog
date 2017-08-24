from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class Contact(FlaskForm):
    name = StringField("Name", [DataRequired('Please Enter Your Name')])
    email = StringField("Email", [DataRequired('Please Enter Your Email Address'), Email('Email Must Be Correct Format')])
    subject = StringField("Subject", [DataRequired('Please Enter a Subject')])
    message = TextAreaField("Message", [DataRequired('Please Enter a Message')])
    submit = SubmitField("Send")

