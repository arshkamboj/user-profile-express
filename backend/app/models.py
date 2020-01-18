from . import ma, db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email')])
    password = PasswordField('password', validators=[InputRequired()])


class RegisterForm(FlaskForm):
    firstName = StringField('firstName', validators=[InputRequired(), Length(min=2, max=50)])
    lastName = StringField('lastName', validators=[InputRequired(), Length(min=2, max=50)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=100)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=100)])


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    publicId = db.Column(db.String(100))
    firstName = db.Column(db.String(40))
    lastName = db.Column(db.String(40))
    email = db.Column(db.String(40))
    password = db.Column(db.String(255))

    def __init__(self, publicId, firstName, lastName, email, password):
        self.publicId = publicId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r %r>' % (self.email, self.lastName)


class ProfileImage(db.Model):
    __tablename__ = 'profileImage'
    id = db.Column(db.Integer, primary_key=True)
    publicId = db.Column(db.String(100))
    imageLocation = db.Column(db.String(200))

    def __init__(self, publicId, imageLocation):
        self.publicId = publicId
        self.imageLocation = imageLocation

# user Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'publicId', 'firstName', 'lastName', 'email', 'password')


# Init schema
userSchema = UserSchema()
usersSchema = UserSchema(many=True)