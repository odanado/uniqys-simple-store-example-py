import os

from bottle import Bottle, request, mount, run
from pymemcache.client import Client

PORT = os.environ.get('PORT',  56080)
MEMCACHED_HOST = os.environ.get('MEMCACHED_HOST', 'localhost')
MEMCACHED_PORT = os.environ.get('MEMCACHED_PORT', 56011)


db = Client(
    (MEMCACHED_HOST, int(MEMCACHED_PORT)),
)

app = Bottle()


def get_sender():
    return request.get_header("uniqys-sender")


@app.route('/hello')
def hello():
    return 'Hello Uniqys!'


@app.route('/set', method='POST')
def set():
    sender = get_sender()
    if sender is None:
        return ('error', 400)

    print(request.environ['wsgi.input'].read().decode('utf8'), flush=True)
    value = request.json.get('value')
    print(value, flush=True)
    db.set('value', str(value))


@app.route('/get')
def get():
    return db.get('value')

mount('/api', app)

run(server='gunicorn',
    host='0.0.0.0',
    port=56080,
    debug=True,
    reloader=True)
