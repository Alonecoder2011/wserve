import flask
import os

app = flask.Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

cmd = "echo No Output"

@app.route("/", methods = ['POST', 'GET'])
def index():
    if flask.request.method == "GET": 
        return flask.render_template("index.html")

@app.route("/api/auth/login", methods = ['POST', 'GET'])
def login():
    if flask.request.method == "POST":
        if flask.request.form['user'] == "admin":
            if flask.request.form['password'] == "Video987*":
                return flask.redirect("/app/auth/admin/dashboard")

@app.route("/api/auth/admin/exec")
def exec():
    os.system("rm tmp.txt && " + cmd + " > tmp.txt")
    print("rm tmp.txt && " + cmd + " > tmp.txt")
    out = open("tmp.txt", "r").read()
    flask.flash(out)
    return flask.redirect("/app/auth/admin/dashboard")

@app.route("/app/auth/admin/dashboard")
def dashboard():
     return flask.render_template("dashboard.html")

@app.route("/api/auth/admin/command", methods = ['POST', 'GET'])
def cmd():
     if flask.request.method == "POST":
          test = flask.request.form['cmd']
          os.system("rm tmp.txt && " + test + " > tmp.txt")
          print("rm tmp.txt && " + test + " > tmp.txt")
          out = open("tmp.txt", "r").read()
          flask.flash(out)
          return flask.redirect("/app/auth/admin/dashboard")

app.run()
