from flask import Flask, render_template, request
#form, update, list itself

list = []

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():

        if request.method == "GET":
            return render_template('index.html', list=list)

        elif request.method == "POST":

            todoz  = request.form['todo']
            list.append(todoz)

            return render_template('index.html', list=list)

    return app
