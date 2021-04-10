from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
   name = 'Matthew'
   return render_template("index.html", name=name)



@app.route('/welcome')
def welcome():
   return render_template("welcome.html")
