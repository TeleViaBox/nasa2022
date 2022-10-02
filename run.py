# -*- coding: UTF-8 -*-
from app import app

@app.route('/')
def index():
    return 'Flask Api started'

if __name__ == '__main_':
    app.run(host='0.0.0.0', port = 3000, debug = False)
