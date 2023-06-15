from flask import Flask, render_template, request, redirect
from users import USER

app = Flask(__name__)
app.secret_key = "secret tunnel"
#connect the DB here?


#default screen which is the screen that shows All Users from DB listed
@app.route('/')
def all_users():
    return redirect('/readAll')

#gets us the list of users in the table
@app.route('/readAll')
def users():
    return render_template("readAll.html", users = USER.get_all())

#takes user to add a new entry page to fill in form
@app.route('/create/added')
def added():
    return render_template("create.html")

#adds new entry into table and takes user back to the readAll page with list
@app.route('/create/new', methods=['POST'])
def new():
    print(request.form)
    USER.save(request.form)
    return redirect('/readAll')

if __name__=="__main__":  
    app.run(debug=True, port=5001)
