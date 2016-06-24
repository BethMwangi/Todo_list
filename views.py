from flask import render_template, request,redirect
from models import Category, Todo, Priority, db
from todoapp import app


@app.route('/')
def list_all():
    return render_template(
        'list.html',
        categories=Category.query.all(),
        todos=Todo.query.join(Priority).order_by(Priority.value.desc())    
    )





#    return '<h1>My name is Beth</h1>'