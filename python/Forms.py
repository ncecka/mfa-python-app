from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField

class LoginForm(FlaskForm):
      username = StringField('username')
      otp = StringField('otp')

class RegisterByUserForm(FlaskForm):
      id = StringField('id')
      username = StringField('username')
      otp = StringField('otp')

class AddAccountForm(FlaskForm):
      username = StringField('username')
      accountowner = StringField('accountowner')
      grouplist = StringField('grouplist')

class VerifyAccountForm(FlaskForm):
      username = StringField('username')
      accountowner = StringField('accountowner')
      isadaccount = BooleanField('isadaccount')

class RemoveAccountForm(FlaskForm):
      username = StringField('username')

class RegisterByAdminForm(FlaskForm):
      username = StringField('username')
      accountowner = StringField('accountowner')
      isadaccount = BooleanField('isadaccount')

class UnregisterAccountForm(FlaskForm):
      username = StringField('username')