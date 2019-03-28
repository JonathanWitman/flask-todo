from flask import Flask, render_template, request
from . import db
import datetime
#form, update, list itself

list = []

def create_app():
    app = Flask(__name__)

#    app.config.from_mapping(
#        SECRET_KEY='dev',
#        DB_NAME='todo',
#        DB_USER='todo_user'

#    )

#    db.init_db()

    @app.route('/', methods=['GET', 'POST'])
    def index():

        if request.method == "GET":
            return render_template('index.html', list=list)

        elif request.method == "POST":

            new_todo  = request.form['todo']

            comp_todo = new_todo + " created on " + str(datetime.datetime.now())

            db.init_db()
            db.insert(comp_todo)
            db.retrieve(comp_todo)

            list.append(comp_todo)

            return render_template('index.html', list=list)

    @app.route('/database')
    def datab():

        get_db()
#        close_db()

    return app
