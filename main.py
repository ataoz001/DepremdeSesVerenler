# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, static_folder='staticFiles')

with open('list_var.txt') as f:
    contents = f.readlines()

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route('/')
def index():
    return render_template('index.html', contents=contents)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
