from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['secret_key'] = '7e752171d960ffdaf5e5e0490b7684038e2265e444f4def378d923984f3b8400'
Bootstrap(app)

from . import routes
