from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hi_person(name):
    return render_template('template.html',
                           name=name.title())
    
@app.route("/jedi/<firstname>/<lastname>")
def hi_jedi(firstname, lastname):
    return render_template('jedi.html',
                           name=firstname,
                          jediname=(lastname[:3] + firstname[:2]))

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))