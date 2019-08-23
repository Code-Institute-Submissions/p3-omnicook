from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

app = Flask(__name__)

# Initialize selected DB connection
# connection = pymysql.connect(
#     host='localhost', # IP address of the database; localhost means "the local machine"
#     user="admin",  #the mysql user
#     password="password", #the password for the user
#     database="Chinook" #the name of database we want to use
# )

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipe/add')
def add_recipe():
    return render_template("recipe_add.html")

@app.route('/recipe/edit')
def edit_recipe():
    return render_template("recipe_edit.html")
    
@app.route('/recipe')
def view_recipe():
    return render_template("recipe_view.html")
    
@app.route('/recipe/delete')
def delete_recipe():
    return render_template("recipe_delete.html")

# Boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)