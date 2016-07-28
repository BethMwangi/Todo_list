

from flask import Flask
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://blossomciku:coding101@localhost/todoapp'
app.secret_key= 'bettyme'

from views import *

if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    


