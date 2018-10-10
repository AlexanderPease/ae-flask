from flask import current_app as app
from flask import Blueprint, redirect, request, render_template, url_for
from flask import jsonify, make_response
from flask_login import current_user, login_user
from mongoengine.errors import NotUniqueError

from app.forms.application import ApplicationEmailForm, ApplicationFullForm
from app.forms.login import LoginForm
from app.forms.newsletter import NewsletterForm
from werkzeug.security import generate_password_hash
from app.models.lead import Lead
from app.models.user import User

mod = Blueprint('public', __name__)

LOCAL_COST = dict(
    uk='approx. £9.000',
    de='approx. €10.000',
    dk='approx. 75.000 DKK'
)


@app.route('/')
@app.route("/<any('uk', 'de', 'dk'):country>")
def index(country=None):
    local_cost = LOCAL_COST.get(country)

    return render_template(
        'public/index.html',
        form=NewsletterForm(),
        navbar_sticky=True,
        navbar_get_started=True,
        country=country,
        local_cost=local_cost)


@app.route('/apply', methods=['GET', 'POST'])
def application_email():
    form = ApplicationEmailForm()

    if form.validate_on_submit():
        # Create new user
        new_user = User()
        form.populate_obj(new_user)
        new_user.password_hash = generate_password_hash(form.password.data)
        new_user.save()

        # Log in new user
        login_user(new_user)
        return redirect(url_for('application_full'))

    return render_template(
        'public/application_email.html',
        form=form,
        step=1,
        fbad_event=('trackCustom', 'StartRegistration')
    )


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
        step=2,
        fbad_event=('trackCustom', 'CompleteRegistrationEmail')
    )


@app.route('/apply/success')
def application_success():
    return render_template(
        'public/application_success.html',
        step=3,
        fbad_event=('track', 'CompleteRegistration'),
        gad_event=True
    )


@app.route('/lead', methods=['POST'])
def newsletter_lead():
    try:
        email = request.form.get('email')
    except Exception:
        return dict(code=400, message='email not found')

    try:
        Lead(email=email).save()
    except NotUniqueError:
        pass  # In future could tailor response message

    response = dict(code=200, message='success')
    return make_response(jsonify(response), response.get('code'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.user)
        login_user(form.user)
        if 'admin' in current_user.permissions:
            return redirect(url_for('admin.index'))
        return redirect(url_for('index'))

    return render_template(
        'public/login.html',
        form=form)
