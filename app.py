from flask import Flask, render_template, url_for

#Setting up the application. 
#The __name__ argument helps Flask understand the location of the current script so it can set up necessary features (like debugging) and resources.
app = Flask(__name__)

#Creating an index route 
@app.route('/')

def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)