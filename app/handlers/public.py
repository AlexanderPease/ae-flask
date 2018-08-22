from flask import current_app as app
from flask import (
    Blueprint, jsonify, redirect, render_template, request,
    send_from_directory, session, url_for)

mod = Blueprint('public', __name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'