from flask_app import app
from flask import render_template,redirect,request,session,flash,Flask
from flask_app.models.users_model import USER


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

# new route going from show button on readAll.html to the readOne.html
@app.route('/readOne/<int:id>')
def show_one(id):
    #command to view readOne.html

    return render_template('readOne.html', user = USER.get_one({'id':id}))

# new route going from readOne to the edit.html
@app.route('/edit/<int:id>')
def editView(id):
    #command to view edit.html

    return render_template('edit.html', user = USER.get_one({'id':id}))

# edit the user data
@app.route('/update', methods=['POST'])
def updating():
    #command to view edit.html
    USER.update(request.form)
    return redirect('/readAll')


# new route to delete targeted user by pressing button on readAll.html, then refreshes itself to sho updated readAll.html page(goes back to same current home page, but show's list with deleted user gone)
@app.route('/delete/<int:id>')
def remove(id):
    #command to delet?
    USER.delete({'id':id})
    # USER.delete(id)

    return redirect('/readAll')