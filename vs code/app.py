from flask import Flask,render_template,url_for,flash,redirect
import con_fun as connect

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/admin-login')
def admin():
    return render_template("admin_login.html")

@app.route('/contactor-login')
def contractor():
    return render_template("con_login.html")



@app.route('/worker-login')
def worker():
    return render_template("work_login.html")


@app.route('/table')
def table():
    data = connect.table_2()
    return render_template("tables.html",result=data)

