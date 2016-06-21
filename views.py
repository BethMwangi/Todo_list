from todoapp import app

@app.route('/')
def index():
    return '<h1>My name is Beth</h1>'