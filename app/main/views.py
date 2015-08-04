from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app, flash
from .. import db
from ..models import Staff, User, Nationality
from ..email import send_email
from . import main
from .forms import NameForm, RegistrationForm
from flask.ext.login import login_required

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        staff = Staff.query.filter_by(username=form.name.data).first()
        if staff is None:
            staff = Staff(username=form.name.data)
            db.session.add(staff)
            session['known'] = False
            send_email(current_app.config['RD_ADMIN'], 'New Registration', 'mail/test', staff=staff)
        else:
            session['known'] = True
            flash('Name not added')
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'))

@main.route('/staff/<name>')
def staff(name):
    form = NameForm()
    return render_template('staff.html', name=name)


@main.route('/new-register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    form.nationality.choices = [(n.id, n.country) for n in Nationality.query.order_by('country')]
    if form.validate_on_submit():
        user = User.query.filter_by(phone_1=form.phone_1.data).first()
        if user is None:
            user = User(name=form.name.data, phone_1=form.phone_1.data,
                    phone_2=form.phone_2.data, notes=form.notes.data, postcode=form.postcode.data)
            db.session.add(user)
            id_number = User.query.filter_by(name=form.name.data).first().id
            flash('Registered: %s - ID#%d' % (form.name.data, id_number))
            return redirect(url_for('.registration'))
        else:
            flash('Phone Number (#1) is already registered')
    return render_template('register.html', form=form)

@main.route('/secret')
@login_required
def secret():
    return("Hahah")