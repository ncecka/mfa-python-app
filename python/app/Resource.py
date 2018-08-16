import requests, uuid
from ApplicationService import ApplicationService
from app import app
from Constants import Constant
from CompanyService import CompanyService
from Forms import LoginForm, RegisterByUserForm, AddAccountForm, VerifyAccountForm, RemoveAccountForm, RegisterByAdminForm, UnregisterAccountForm
from flask import flash, render_template, request, session, redirect
from flask_api import status
from flask_socketio import SocketIO, emit
from wtforms import Form, validators

clients = dict()
socketio = SocketIO(app)
appService = ApplicationService()
companyService = CompanyService()

@app.route('/', methods=['GET','POST'])
def index():
    return redirect("/login", code=302)

@app.route('/login', methods=['GET','POST'])
def Login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
       result = appService.login(form.username.data, form.otp.data)
       flash(result)
    return render_template('login.html', title='Login', form=form)

@app.route('/registration', methods=['GET','POST'])
def Registration():
    form = RegisterByUserForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
       result = appService.registration(form.username.data, form.id.data, form.otp.data)
       flash(result)
    return render_template('registration.html', title='Registration', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
def AddAccount():
    form = AddAccountForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
       result = companyService.addAccount(form.username.data, form.accountowner.data, form.grouplist.data)
       flash(result)
    return render_template('dashboard.html', title='Dashboard_AddNewAccount', form=form)

@app.route('/dashboard-verify', methods=['GET', 'POST'])
def VerifyAccount():
    form = VerifyAccountForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
       result = companyService.verifyAccount(form.username.data, form.accountowner.data, form.isadaccount.data)
       flash(result)
    return render_template('dashboard-verify.html', title='Dashboard_VerifyAccount', form=form)

@app.route('/dashboard-remove', methods=['GET', 'POST'])
def RemoveAccount():
    form = RemoveAccountForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
       result = companyService.removeAccount(form.username.data)
       flash(result)
    return render_template('dashboard-remove.html', title='Dashboard_RemoveAccount', form=form)

@app.route('/dashboard-regacc', methods=['GET', 'POST'])
def RegisterAccountByAdmin():
    form = RegisterByAdminForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        result = appService.registerAccountByAdmin(form.username.data, form.accountowner.data, form.isadaccount.data)
        flash(result)
    return render_template('dashboard-regacc.html', title='Dashboard_RegisterAccountByAdmin', form=form)

@app.route('/dashboard-unregister', methods=['GET', 'POST'])
def UnregisterAccount():
    form = UnregisterAccountForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        result = appService.unregister(form.username.data)
        flash(result)
    return render_template('dashboard-unregister.html', title='Dashboard_UnregisterAccount', form=form)

def GetBarcode():
       sessionId = uuid.uuid4()
       session['uid'] = str(sessionId)
       result = appService.getbarcodeimage(sessionId)
       return result
app.jinja_env.globals.update(scanbarcode=GetBarcode)


@app.route('/login-post-url', methods=['POST'])
def empty_view():
    sessionID = request.headers.get('session')
    username = request.headers.get('username')
    trackerID = request.headers.get('tracker')
    result = appService.trackerValidation(trackerID, username)
    if result == True :
       socketio.emit('message', {'result': 'OK'}, room=clients[sessionID])
    else: print("Tracker is invalid.")
    content = ""
    return content, status.HTTP_200_OK

@socketio.on('connect')
def connected():
    socket_id = request.sid
    clients[session['uid']] = socket_id

@socketio.on('disconnect')
def disconnected():
    del clients[session['uid']]