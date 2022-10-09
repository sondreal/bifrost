import random

import requests
from flask import Flask


loadbalancer = Flask(__name__)

BLUE_BACKEND = ['localhost:8081', 'localhost:8082']
GREEN_BACKEND = ['localhost:9081', 'localhost:9082']

@loadbalancer.route('/')
def router():
    host_header = requests.headers['Host']
    if host_header == 'www.blue.no':
        response = requests.get(f'https://{random.choice(BLUE_BACKEND)}')
        return response.content, response.status_code
    elif host_header == 'www.green.no':
        response = requests.get(f'https://{random.choice(GREEN_BACKEND)}')
        return response.content, response.status_code
    else:
        return 'Not Found', 404