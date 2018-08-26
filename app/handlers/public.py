from flask import current_app as app
from flask import (
    Blueprint, jsonify, redirect, render_template, request,
    session, url_for)

from app.forms.application import (
    ApplicationEmailForm, ApplicationFullForm)

mod = Blueprint('public', __name__)


@app.route('/')
def index():
    return render_template('public/index.html')


@app.route('/apply', methods=['GET', 'POST'])
def application_email():
    form = ApplicationEmailForm()

    if form.validate_on_submit():
        pass
    return render_template(
        'public/application_email.html',
        form=form,
        step=1)


@app.route('/apply-2')
def application_full():
    form = ApplicationFullForm()

    if form.validate_on_submit():
        pass
    return render_template(
        'public/application_full.html',
        form=form,
        step=2)


@app.route('/apply/success')
def apply():
    return render_template('public/application_success.html')


