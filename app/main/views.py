from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app, flash
from .. import db
from ..models import Staff, User, Nationality, Company, Role
from ..email import send_email
from . import main
from .forms import NameForm, NationalityAddForm, RoleAddForm
from flask.ext.login import login_required, current_user

@main.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated():
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login'))

@main.route('/nationality', methods=['GET', 'POST'])
def add_nationality():
    form = NationalityAddForm()
    if form.validate_on_submit():
        db.session.add(Nationality(form.name.data))
        flash('Nationality Added: ' + form.name.data)
        return redirect(url_for('main.add_nationality'))
    return render_template('nationality.html', form=form)

@main.route('/roles', methods=['GET', 'POST'])
def add_role():
    form = RoleAddForm()
    role = Role.query.all()
    if form.validate_on_submit():
        exist = Role.query.filter_by(name=form.name.data).first()
        if exist:
            flash('Role ' + form.name.data + ' already exists')
            return redirect(url_for('main.add_role'))
        else:
            flash('Role ' + form.name.data + ' added')
            db.session.add(Role(form.name.data, form.department.data, form.rate.data))
            return redirect(url_for('main.add_role'))
    return render_template('role.html', form=form, role=role)

@main.route('/secret')
@login_required
def secret():
    return(render_template('test.html'))
