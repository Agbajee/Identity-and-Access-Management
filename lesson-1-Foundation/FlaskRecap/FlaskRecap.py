#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from encodings.utf_8 import encode
from flask import Flask, request, jsonify, abort
import jwt
import base64
import json
from jose import jwt
from urllib.request import urlopen

def get_token_auth_header():
# check if authorization is not in request
    if 'Authorization' not in request.headers:
        abort(401)
# get the token   
    auth_header = request.headers['Authorization']
    header_parts = auth_header.split(' ')
# check if token is valid
    if len(header_parts) != 2:
        abort(401)
    elif header_parts[0].lower() != 'bearer':
        abort(401) 

    return header_parts[1]

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
    jwt = get_token_auth_header()
    print(jwt)
    return "not implemented"

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

