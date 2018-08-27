from flask import current_app as app
from flask import Blueprint, redirect, render_template, session, url_for
from flask_login import current_user

from app.forms.application import ApplicationEmailForm, ApplicationFullForm
from app.forms.newsletter import NewsletterForm
from app.lib.password import get_password_hash
from app.models.lead import Lead
from app.models.user import User

mod = Blueprint('public', __name__)


@app.route('/')
def index():
    return render_template(
        'public/index.html',
        form=NewsletterForm())


@app.route('/apply', methods=['GET', 'POST'])
def application_email():
    form = ApplicationEmailForm()

    if form.validate_on_submit():
        # Create new user
        new_user = User()
        form.populate_obj(new_user)
        new_user.password_hash = get_password_hash(form.password.data)
        new_user.save()

        # Log in new user
        login_user(new_user)
        return redirect(url_for('application_full'))

    return render_template(
        'public/application_email.html',
        form=form,
        step=1)


@app.route('/apply-2', methods=['GET', 'POST'])
def application_full():
    form = ApplicationFullForm()

    if form.validate_on_submit():
        # Update current user
        form.populate_obj(current_user)
        current_user.save()
        return redirect(url_for('application_success'))

    return render_template(
        'public/application_full.html',
        form=form,
        step=2)


@app.route('/apply/success')
def application_success():
    return render_template(
        'public/application_success.html',
        step=3)


@app.route('/lead/create', methods=['POST'])
def newsletter_lead():
    form = NewsletterForm()

    if form.validate_on_submit():
        lead = Lead()
        form.populate_obj(lead)
        return redirect(url_for('application_email'))

    return redirect(url_for('index'))



