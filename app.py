from flask import Flask, render_template, url_for
from flash_sqlalchemy import SQLAlchemy
from datetime import datetime

#Setting up the application. 
#The __name__ argument helps Flask understand the location of the current script so it can set up necessary features (like debugging) and resources.
app = Flask(__name__)
#Telling our app where our database is located
#Using 3 forward slashes to avoid specifying the exact file location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test/db'
#Initializing the database
db = SQLAlchemy(app)

#Creating a model
class Todo(db.model):
    id = db.Column(db.Integer, primary_key = True)
    #Setting nullable to false because we dont want user to leave this blank
    content = db.Column(db.String(200), nullable = False)
    #For book keeping, not for the user to access to
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    #Function that returns a string everytime we create a new element
    def __repr__(self):
        #Everytime we make a new element, it is going to return task and the id of the task created
        return '<Task %r>' % self.id




#Creating an index route 
@app.route('/')

def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)