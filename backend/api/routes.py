from . import app


@app.get('/')
def index():
    return {'hello': 'world!'}

