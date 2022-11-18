from flask import Flask, render_template,request,flash,redirect,url_for,session
import sqlite3

app = Flask(__name__)
app.secret_key="123"

con=sqlite3.connect("database.db")
con.execute("create table if not exists users(pid integer primary key,name text,mail text,contact integer,password text)")
con.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    try:
        if request.method=='POST':
            name=request.form['name']
            password=request.form['password']
            con=sqlite3.connect("database.db")
            con.row_factory=sqlite3.Row
            cur=con.cursor()
            cur.execute("select * from users where name=? and password=?",(name,password))
            data=cur.fetchone()

            if data:
                session["name"]=data["name"]
                session["password"]=data["password"]
                return redirect("users")
            else:
                flash("Username and Password Mismatch","danger")
            return redirect(url_for("index"))

    except:
        flash("Chech Your Name And Password")   

@app.route('/users',methods=["GET","POST"])
def customer():
    return render_template("customer.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        try:
            name=request.form['name']
            mail=request.form['mail']
            contact=request.form['contact']
            password=request.form['password']
            con=sqlite3.connect("database.db")
            cur=con.cursor()
            cur.execute("insert into users(name,mail,contact,password)values(?,?,?,?)",(name,mail,contact,password))
            con.commit()
            flash("Record Added  Successfully","success")
        except:
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("index"))
            con.close()

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route('/apply',methods=['GET','POST'])
def apply():
    return render_template('apply.html')

if __name__ == '__main__':
    app.run()
