#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from encodings.utf_8 import encode
from flask import Flask, request, jsonify, abort
import jwt
import base64
import json
from jose import jwt
from urllib.request import urlopen

AUTH0_DOMAIN = 'devagbaje.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'image'
AUTH_LINK = 'https://devagbaje.us.auth0.com/authorize?audience=image&response_type=token&client_id=zHXITxdbfKqY1vYaaZSzAPqGxLMJVn4j&redirect_uri=https://127.0.0.1:8080/login-result'

app = Flask(__name__)

greetings = {
            'en': 'hello', 
            'es': 'Hola', 
            'ar': 'مرحبا',
            'ru': 'Привет',
            'fi': 'Hei',
            'he': 'שלום',
            'ja': 'こんにちは'
            }

@app.route('/', methods=['GET'])
def hello():
    payload = {'school':'udacity'}
    algo = 'HS256'
    secret = 'learning'

    encoded_jwt = jwt.encode(payload, secret, algorithm=algo)

    return encoded_jwt

@app.route('/header', methods=['GET'])
def headers():
    auth_header = request.headers['Authorization']

    # get the token
    header_parts = auth_header.split(' ')[1]
    print(header_parts)

    return header_parts

@app.route('/greeting', methods=['GET'])
def greeting_all():
    return jsonify({'greetings': greetings})

@app.route('/greeting/<lang>', methods=['GET'])
def greeting_one(lang):
    print(lang)
    if(lang not in greetings):
        abort(404)
    return jsonify({'greeting': greetings[lang
    ]})

@app.route('/greeting', methods=['POST'])
def greeting_add():
    info = request.get_json()
    if('lang' not in info or 'greeting' not in info):
        abort(422)
    greetings[info['lang']] = info['greeting']
    return jsonify({'greetings':greetings})

