# loadbalancer.py

import random

import requests
import yaml
from flask import Flask


loadbalancer = Flask(__name__)

def load_configuration(path):
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config

config = load_configuration('loadbalancer.yaml')

BLUE_BACKEND = ['localhost:8081', 'localhost:8082']
GREEN_BACKEND = ['localhost:9081', 'localhost:9082']

@loadbalancer.route('/')
def router():
    host_header = requests.headers['Host']
    for entry in config['hosts']:
        if host_header == entry['host']:
            response = requests.get(f'http://{random.choice(entry["servers"])}')
            return response.content, response.status_code
    return 'Not Found', 404

@loadbalancer.route('/<path>')
def path_router(path):
    for entry in config['paths']:
        if ('/' + path) == entry['path']:
            response = requests.get(f'http://{random.choice(entry["servers"])}')
            return response.content, response.status_code
    return 'Not Found', 404

