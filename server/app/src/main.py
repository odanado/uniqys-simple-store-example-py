import os

from bottle import request, route, run
from pymemcache.client import Client

PORT = os.environ.get('PORT',  56080)
MEMCACHED_HOST = os.environ.get('MEMCACHED_HOST', 'localhost')
MEMCACHED_PORT = os.environ.get('MEMCACHED_PORT', 56011)


db = Client(
    (MEMCACHED_HOST, int(MEMCACHED_PORT)),
)


def get_sender():
    return request.get_header("uniqys-sender")


@route('/hello')
def hello():
    return 'Hello Uniqys!'


@route('/set/:value', method='POST')
def set(value):
    sender = get_sender()
    if sender is None:
        return ('error', 400)

    db.set('value', str(value))


@route('/get')
def get():
    return db.get('value')


run(host='0.0.0.0',
    port=56080)
